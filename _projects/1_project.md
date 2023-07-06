---
layout: page
title: Turbulence in Plasmas
description: Inverse cascade in gyrofluids
img: assets/img/jz_bal_B11_t11000_z0.png
importance: 1
category: work
---

In this project the idea is to model ion and sub-ion scales that one finds in solar wind turbulence of forward and backward propagating Alfvèn waves (AW). Solar wind is ejected from the sun and propagets through heliosphere before reaching the Earth's magnetosphere. Of particular interest for us was Kinetic Alfvèn Wave (KAW) turbulence which is a oblique dispersive wave that continues the AW spectrum to the small scales. There are various questions in solar wind community related to spectral breaks at ion scales and heating of solar wind all the way down to electron scales. These scales are related to motion of charged particles in self-consistent fields.  

<div class="row justify-content-sm-center">
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/solarwind.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/SPP-shown-along-its-orbit.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-3 mt-3 mt-md-0">
        {% include figure.html path="assets/img/Wicksimbalance.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    On the left, we have artists image of solar wind emenating from the sun. Middle, shows schematics of [Solar Parker Probe](https://www.nasa.gov/content/goddard/parker-solar-probe) mission. Right, forward and backward propagating AW spectra measured by another spacecraft
</div>

We use a model (gyrofluid) that assumes isothermal electrons and is obtained from kinetics under a set of approximations. The motivation behind using gyrofluids is that they are much cheaper to run than gyrokinetic or full kinetic code. The two important quantities of interest are `total energy` and `Generalized Cross Helicity` GCH

$$
	E \sim \int d^3\,x\, ( E_+ + E_- ) 
$$

and

$$
	E_{GCH} \sim \int d^3\,x\, ( E_+ - E_- )/V_{ph},
$$

where $$V_{ph}$$ is the KAW phase velocity. The system of equations is modelled numerically using pseuspectral code. We inject forward $$E_+$$ and backward $$E_-$$ propagating waves at a range of small wavenumbers and observe the `inverse transfer` of GCH. 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, *bled* for your project, and then... you reveal its glory in the next row of images.


<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left panel: A slice of 3D FFT of Elsasser potential displaying bands corresponding to resonant frequencies. Right panel: Resonance condition
</div>

Our work culminates with showing small nonlinear parameter which controls the regime. If the turbulence gets too strong the simple 3-wave resonance picture is washed out

$$
\chi_f\sim\frac{(k_f v_{ph})^{-1}}{\tau_{NL}} \sim\epsilon_E^{1/3}k_\perp^{1/3}\beta_e^{1/2}k_\|^{-1},
$$

{% raw %}
```html
<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
```
{% endraw %}
