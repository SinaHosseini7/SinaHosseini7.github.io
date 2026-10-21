---
layout: page
title: Research
permalink: /research/
---
## Overview

Most of my work deals with one problem: heat crossing a boundary where it should not. In a cryogenic tank, heat leaking in through supports and nozzles boils off the stored liquid. Next to a molten-metal ladle, heat reaching a battery compartment can damage the batteries. In buildings, heat lost through walls wastes energy. I work on these problems from two sides. I model the heat paths with CFD, and I work with the materials that block them, mainly aerogels and vacuum-based insulation. I want to study them with better models and better-tested materials.

## Heat Transfer & CFD of Thermal-Fluid Systems {#heat-transfer-cfd}

### What I have done

For Mobarakeh Steel Co., I ran all 16 cases of a conduction, convection, and radiation model of a battery-powered ladle carrier in FloEFD, with geometry from CATIA and SolidWorks ([project](/projects/mobarakeh-steel-heat-transfer/)). For the Asaluyeh LPG lines, I simulated hot-air injection in STAR-CCM+ and FloEFD; the study found that air at about 100 °C and 5–10 m/s prevents ice formation while aerogel blankets replace failed insulation ([project](/projects/lpg-line-aerogel-insulation/)). I also wrote Python modules, including streamline visualization, for a porous-media flow simulator based on Darcy's law ([project](/projects/flow-simulation-software/)).

### What I want to explore

How far can steady-state, coarse-mesh CFD be trusted for industrial problems that are really transient, such as a vehicle moving past a hot metal spill? I also want to test surrogate or data-driven models that could replace repeated CFD runs when many design options must be compared.

## Thermal Insulation & Porous Materials {#insulation-porous}

### What I have done

For my BSc thesis, I added silica aerogel to gypsum plaster at several volume fractions and measured the heat-transfer coefficient (Hilton heat conduction unit), compressive strength, and density (Archimedes method) ([project](/projects/aerogel-construction-plaster/)). I also synthesized silica aerogels, characterized them with FTIR and BET, and co-authored two papers on aerogel insulating paints for buildings ([publications](/publications/)). At Nano Sun Abrad, I worked with multilayer insulation (MLI), perlite, and Layered Composite Insulation for Extreme Conditions (LCX) on cryogenic tanks and used a thermal camera to locate thermal bridges at supports, nozzles, bolts, and seams ([project](/projects/storage-tank-thermal-bridges/)).

### What I want to explore

I want to understand how thermal bridges at supports and fasteners limit the real performance of thin, high-performance insulation, and how to design around them. I am also interested in coupled heat and moisture transport in porous insulation on cold lines, where condensation and ice reduce performance.

{% include figure.html src="/assets/img/research/jemt-2023-energy.webp" alt="Line chart of cumulative energy consumption over 12 hours for no insulation and for 0.5, 1, and 2 mm aerogel paint coatings at 5 m/s wind" caption="Simulated cumulative energy use of a test building over 12 hours at 5 m/s wind, for paint coatings 0–2 mm thick (JEMT 2023, CC BY)." %}

## Thermal Management & Energy Storage {#thermal-management-storage}

### What I have done

At Nano Sun Abrad, I validated FloEFD heat-leak models of tanks for liquid oxygen, liquid nitrogen, and liquid CO₂ after construction, by converting the boil-off rate into absorbed heat ([project](/projects/storage-tank-thermal-bridges/)). In the Mobarakeh study, I compared insulation thickness, fan number and speed, and battery layout against a 50 °C limit for batteries next to a ladle wall at about 400 °C ([project](/projects/mobarakeh-steel-heat-transfer/)).

### What I want to explore

I want to study insulation and heat leak in cryogenic storage of hydrogen and LNG, where boil-off sets both cost and safety limits. I am also interested in a design question from the Mobarakeh study: when is passive insulation enough, and when do batteries or electronics near strong heat sources need active cooling?

## Methods & Tools

### Computational

- CFD and heat-transfer simulation: FloEFD, STAR-CCM+
- Python for scientific computing and visualization of simulation results; MATLAB
- Numerical methods, including Darcy's-law porous-media flow
- CAD: CATIA, SolidWorks, Solid Edge

### Experimental

- Synthesis and characterization of nanoporous materials (silica aerogels; FTIR, BET)
- Insulation performance testing: heat-conduction measurement, thermal imaging, boil-off-based heat-leak validation
- Compressive strength and Archimedes density of composite samples
- Laboratory process work (MSc): leaching
- Experimental budget management; literature and patent searches

---

I am open to PhD opportunities on these questions. If you work on related problems, I would be glad to hear from you at [{{ site.data.profile.email }}](mailto:{{ site.data.profile.email }}).
