#!/usr/bin/env python

import os
import sys
import yaml
from datetime import datetime
from scholarly import scholarly
import re
import unicodedata
import difflib


def load_scholar_user_id() -> str:
    """Load the Google Scholar user ID from the configuration file."""
    config_file = "_data/socials.yml"
    if not os.path.exists(config_file):
        print(
            f"Configuration file {config_file} not found. Please ensure the file exists and contains your Google Scholar user ID."
        )
        sys.exit(1)
    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
        scholar_user_id = config.get("scholar_userid")
        if not scholar_user_id:
            print(
                "No 'scholar_userid' found in the configuration file. Please add 'scholar_userid' to _data/socials.yml."
            )
            sys.exit(1)
        return scholar_user_id
    except yaml.YAMLError as e:
        print(
            f"Error parsing YAML file {config_file}: {e}. Please check the file for correct YAML syntax."
        )
        sys.exit(1)


SCHOLAR_USER_ID: str = load_scholar_user_id()
OUTPUT_FILE: str = "_data/citations.yml"
BIB_FIELD_NAME = "googlescholarid"


def get_scholar_citations() -> None:
    """Fetch and update Google Scholar citation data."""
    print(f"Fetching citations for Google Scholar ID: {SCHOLAR_USER_ID}")
    today = datetime.now().strftime("%Y-%m-%d")

    # Check if the output file was already updated today
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r") as f:
                existing_data = yaml.safe_load(f)
            if (
                existing_data
                and "metadata" in existing_data
                and "last_updated" in existing_data["metadata"]
            ):
                print(f"Last updated on: {existing_data['metadata']['last_updated']}")
                if existing_data["metadata"]["last_updated"] == today:
                    print("Citations data is already up-to-date. Skipping fetch.")
                    # still attempt to annotate BibTeX with existing data
                    try:
                        update_bibtex_with_ids("_bibliography/papers.bib", existing_data.get("papers", {}))
                        write_bibid_map("_bibliography/papers.bib", existing_data.get("papers", {}))
                    except Exception as e:
                        print(f"Warning: could not update BibTeX file with scholar ids: {e}")
                    return
        except Exception as e:
            print(
                f"Warning: Could not read existing citation data from {OUTPUT_FILE}: {e}. The file may be missing or corrupted."
            )

    citation_data = {"metadata": {"last_updated": today}, "papers": {}}

    scholarly.set_timeout(15)
    scholarly.set_retries(3)
    try:
        author = scholarly.search_author_id(SCHOLAR_USER_ID)
        author_data = scholarly.fill(author)
    except Exception as e:
        print(
            f"Error fetching author data from Google Scholar for user ID '{SCHOLAR_USER_ID}': {e}. Please check your internet connection and Scholar user ID."
        )
        sys.exit(1)

    if not author_data:
        print(
            f"Could not fetch author data for user ID '{SCHOLAR_USER_ID}'. Please verify the Scholar user ID and try again."
        )
        sys.exit(1)

    if "publications" not in author_data:
        print(f"No publications found in author data for user ID '{SCHOLAR_USER_ID}'.")
        sys.exit(1)

    for pub in author_data["publications"]:
        try:
            pub_id = pub.get("pub_id") or pub.get("author_pub_id")
            if not pub_id:
                print(
                    f"Warning: No ID found for publication: {pub.get('bib', {}).get('title', 'Unknown')}. This publication will be skipped."
                )
                continue

            title = pub.get("bib", {}).get("title", "Unknown Title")
            year = pub.get("bib", {}).get("pub_year", "Unknown Year")
            citations = pub.get("num_citations", 0)

            print(f"Found: {title} ({year}) - Citations: {citations}")

            citation_data["papers"][pub_id] = {
                "title": title,
                "year": year,
                "citations": citations,
            }
        except Exception as e:
            print(
                f"Error processing publication '{pub.get('bib', {}).get('title', 'Unknown')}': {e}. This publication will be skipped."
            )

    # Compare new data with existing data
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r") as f:
                existing_data = yaml.safe_load(f)
        except Exception:
            existing_data = None
    else:
        existing_data = None

    if existing_data and existing_data.get("papers") == citation_data["papers"]:
        print("No changes in citation data. Skipping file update.")
        return

    # Attempt to generate a bib-key -> scholar pub_id mapping (safer than editing .bib)
    bib_path = "_bibliography/papers.bib"
    try:
        # keep the (legacy) attempt to edit BibTeX but also write a safe mapping file
        update_bibtex_with_ids(bib_path, citation_data["papers"])
        write_bibid_map(bib_path, citation_data["papers"])
    except Exception as e:
        print(f"Warning: could not update BibTeX or write bib id map: {e}")

    try:
        with open(OUTPUT_FILE, "w") as f:
            yaml.dump(citation_data, f, width=1000, sort_keys=True)
        print(f"Citation data saved to {OUTPUT_FILE}")
    except Exception as e:
        print(
            f"Error writing citation data to {OUTPUT_FILE}: {e}. Please check file permissions and disk space."
        )
        sys.exit(1)


def normalize_title(s: str) -> str:
    """Normalize titles for fuzzy matching: lower, remove diacritics, punctuation, and collapse whitespace."""
    if not s:
        return ""
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def update_bibtex_with_ids(bib_path: str, papers: dict) -> None:
    """Try to match scholar publications to BibTeX entries by title and add google_scholar_id fields.

    `papers` is a dict mapping pub_id -> {title, year, citations}.
    """
    if not os.path.exists(bib_path):
        print(f"BibTeX file {bib_path} not found, skipping BibTeX annotation.")
        return

    with open(bib_path, "r", encoding="utf-8") as f:
        bib_text = f.read()

    entries = re.split(r'(?=@)', bib_text)
    changed = False

    # Extract titles from bib entries and build normalized map
    bib_titles = []  # list of (index, raw_title, normalized_title, entry_text)
    for i, entry in enumerate(entries):
        if not entry.strip():
            continue
        m = re.search(r'title\s*=\s*\{([^}]*)\}', entry, flags=re.IGNORECASE | re.DOTALL)
        if not m:
            m = re.search(r'title\s*=\s*"([^"]*)"', entry, flags=re.IGNORECASE | re.DOTALL)
        title_in_entry = m.group(1).strip() if m else None
        norm = normalize_title(title_in_entry) if title_in_entry else ""
        bib_titles.append((i, title_in_entry or "", norm, entry))

    # Track which bib entries already have google_scholar_id or are assigned
    assigned_entries = set()
    for idx, raw_title, norm_title, entry_text in bib_titles:
        if re.search(r'google_scholar_id\s*=\s*', entry_text, flags=re.IGNORECASE):
            assigned_entries.add(idx)

    # For each paper, find best matching bib entry using fuzzy matching
    bib_index_to_new_entry = {}
    for pub_id, info in papers.items():
        paper_title = info.get("title", "")
        norm_paper = normalize_title(paper_title)
        best_idx = None
        best_score = 0.0
        for idx, raw_title, norm_title, entry_text in bib_titles:
            if idx in assigned_entries:
                continue
            if not norm_title:
                continue
            # Compute similarity
            score = difflib.SequenceMatcher(None, norm_paper, norm_title).ratio()
            if score > best_score:
                best_score = score
                best_idx = idx

        # Accept match if score high enough
        if best_idx is not None and best_score >= 0.72:
            entry = entries[best_idx]
            # Double-check not already has the field
            # treat old invalid field name or new safe name as already-assigned
            if re.search(r'(?:google_scholar_id|%s)\s*=\s*' % BIB_FIELD_NAME, entry, flags=re.IGNORECASE):
                continue
                entry_body = entry.rstrip()
                m_close = re.search(r"\n\s*}\s*\Z", entry_body, flags=re.DOTALL)
                if m_close:
                    start = m_close.start()
                    before = entry_body[:start]
                    # ensure previous field ends with a comma
                    if not before.rstrip().endswith(','):
                        replacement = ",\n  %s = {{{}}}\n}}\n" % BIB_FIELD_NAME
                        replacement = replacement.format(pub_id)
                    else:
                        replacement = "\n  %s = {{{}}}\n}}\n" % BIB_FIELD_NAME
                        replacement = replacement.format(pub_id)
                    new_entry = before + replacement
                else:
                    # fallback: append field before final brace
                    if entry_body.endswith('}'): 
                        before = entry_body[:-1].rstrip()
                        if not before.rstrip().endswith(','):
                            replacement = ",\n  %s = {{{}}}\n}}\n" % BIB_FIELD_NAME
                            replacement = replacement.format(pub_id)
                        else:
                            replacement = "\n  %s = {{{}}}\n}}\n" % BIB_FIELD_NAME
                            replacement = replacement.format(pub_id)
                        new_entry = before + replacement
                    else:
                        new_entry = entry_body + f"\n  {BIB_FIELD_NAME} = {{{pub_id}}}\n}}\n"

                if new_entry != entry:
                    bib_index_to_new_entry[best_idx] = new_entry
                    assigned_entries.add(best_idx)
                    changed = True
                    print(f"Annotated BibTeX entry (index {best_idx}) for title '{paper_title}' with google_scholar_id={pub_id} (score={best_score:.2f})")

    # Replace any old invalid field usages first (google_scholar_id -> safe name)
    if 'google_scholar_id' in bib_text:
        bib_text = re.sub(r'google_scholar_id\s*=','%s =' % BIB_FIELD_NAME, bib_text)
        entries = re.split(r'(?=@)', bib_text)
    if changed:
        # Replace entries
        for idx, new_entry in bib_index_to_new_entry.items():
            entries[idx] = new_entry
        new_text = "".join(entries)
        with open(bib_path, "w", encoding="utf-8") as f:
            f.write(new_text)
        print(f"Updated BibTeX file {bib_path} with google_scholar_id fields.")
    else:
        print("No BibTeX entries matched for google_scholar_id annotation.")


def write_bibid_map(bib_path: str, papers: dict) -> None:
    """Generate a safe mapping file `_data/bib_ids.yml` mapping BibTeX entry keys to scholar pub_ids.

    This avoids writing custom fields into the BibTeX file (which can break some parsers).
    """
    out_path = "_data/bib_ids.yml"
    if not os.path.exists(bib_path):
        print(f"BibTeX file {bib_path} not found, skipping bib id mapping.")
        return

    with open(bib_path, "r", encoding="utf-8") as f:
        bib_text = f.read()

    # Find entries and their keys and titles
    entries = re.split(r'(?=@)', bib_text)
    bib_info = []  # list of (key, raw_title, normalized_title)
    for entry in entries:
        if not entry.strip():
            continue
        mkey = re.match(r"@\w+\s*\{\s*([^,\s]+)\s*,", entry)
        if not mkey:
            continue
        key = mkey.group(1).strip()
        m = re.search(r'title\s*=\s*\{([^}]*)\}', entry, flags=re.IGNORECASE | re.DOTALL)
        if not m:
            m = re.search(r'title\s*=\s*"([^"]*)"', entry, flags=re.IGNORECASE | re.DOTALL)
        title_in_entry = m.group(1).strip() if m else ""
        norm = normalize_title(title_in_entry) if title_in_entry else ""
        bib_info.append((key, title_in_entry, norm))

    mapping = {}
    used = set()
    for pub_id, info in papers.items():
        paper_title = info.get("title", "")
        norm_paper = normalize_title(paper_title)
        best_key = None
        best_score = 0.0
        for key, raw_title, norm_title in bib_info:
            if not norm_title:
                continue
            if key in used:
                continue
            score = difflib.SequenceMatcher(None, norm_paper, norm_title).ratio()
            if score > best_score:
                best_score = score
                best_key = key
        if best_key and best_score >= 0.7:
            mapping[best_key] = pub_id
            used.add(best_key)
            print(f"Mapped bib key '{best_key}' to scholar pub_id {pub_id} (score={best_score:.2f})")

    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            yaml.dump(mapping, f, sort_keys=True)
        print(f"Wrote BibTeX key -> scholar pub_id map to {out_path}")
    except Exception as e:
        print(f"Error writing bib id map to {out_path}: {e}")


if __name__ == "__main__":
    try:
        get_scholar_citations()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
