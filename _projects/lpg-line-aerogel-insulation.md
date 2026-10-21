---
title: "Simulating Online Replacement of Aerogel Insulation on Asaluyeh LPG Lines"
summary: "Simulating hot-air injection around a −40 °C LPG pipe so that failed insulation can be replaced with aerogel blankets without ice forming."
group: academic
order: 1
featured: true
role: "Research Assistant"
organization: "University of Zanjan"
period: "2019 – 2020"
theme: insulation-porous
tools: [STAR-CCM+, FloEFD, CATIA]
cover: /assets/img/projects/lpg-line-aerogel-insulation/cover.webp
cover_alt: "Simulated relative-humidity field around an LPG pipe section, with colorbar"
description: "Simulating hot-air injection around a −40 °C LPG pipe so that failed insulation can be replaced with aerogel blankets without ice forming."
image: { path: /assets/img/projects/lpg-line-aerogel-insulation/cover.webp, alt: "Simulated relative-humidity field around an LPG pipe section, with colorbar" }
outputs:
  - { label: "Conference paper (in Persian)", url: "https://civilica.com/doc/1156091/" }
---
## Motivation

On the LPG lines at Asaluyeh, pipes run at about −40 °C under rigid polyurethane insulation. The polyurethane sections have seams, and over time humid air reaches the pipe through them and freezes into ice. Replacing polyurethane takes so long per meter of pipe that it cannot be done while the line is running. Aerogel blankets can be fitted much faster, but only if no ice forms on the cold pipe during the swap. My advisors asked whether hot air from a blower could keep the exposed surface dry for long enough.

## Approach

I built a full pipe section in CATIA, including the insulation gap or seam, the blower, and the position of its nozzle. In STAR-CCM+ and FloEFD, I modeled flow and heat transfer in both steady-state and transient runs. I varied the air temperature from 5 to 100 °C and the air velocity from 4 to 12 m/s. Ambient temperature and humidity came from local meteorological records. I judged ice risk by comparing the pipe-surface temperature with the dew point and 0 °C, together with the local relative humidity near the surface.

## Results

In the simulations, blowing air at about 100 °C and 5–10 m/s during replacement with aerogel blankets prevented ice formation. This points to a way of replacing failed insulation without shutting the line down. The work was a simulation study and was not tested in the field.

{% include figure.html src="/assets/img/projects/lpg-line-aerogel-insulation/geometry.webp" alt="Rendered CAD model of an LPG pipe with yellow polyurethane insulation and a gray conical hot-air device around it" caption="CATIA model from the paper: the pipe with its old polyurethane insulation (yellow) and the conical hot-air device at the edge of the insulation." %}

{% include figure.html src="/assets/img/projects/lpg-line-aerogel-insulation/field.webp" alt="Simulated relative-humidity contours and air-temperature isolines around the LPG pipe, with colorbars" caption="Simulated relative humidity (contours) and air temperature (isolines) around the exposed pipe section while hot air flows from the device." %}

{% include figure.html src="/assets/img/projects/lpg-line-aerogel-insulation/condensation-no-air.webp" alt="Simulated condensation on an exposed LPG pipe section without hot-air blowing" caption="Simulated condensation on the exposed pipe without hot air. This is the problem the hot-air device is meant to prevent." %}

## My contribution

I built the geometry, set up and ran the simulations, processed the results, and wrote parts of the paper with my co-authors, Dr. Hasan Bargozin and Dr. Taher Yousefi Amiri. I presented the work orally at the National Conference of Chemical Engineering and Nanotechnology in 2020.
