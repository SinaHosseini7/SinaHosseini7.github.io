---
title: "Reducing Thermal Bridges in Cryogenic Storage-Tank Insulation"
summary: "Redesigning supports, nozzles, and insulation of vacuum-insulated cryogenic tanks, guided by FloEFD models validated against boil-off measurements."
group: industry
order: 1
featured: true
role: "Head of Research & Development"
organization: "Nano Sun Abrad Co."
period: "2023 – 2025"
theme: insulation-porous
tools: [FloEFD, SolidWorks, Solid Edge, Thermal imaging]
cover: /assets/img/projects/storage-tank-thermal-bridges/cover.webp
cover_alt: "Cryogenic storage tank under construction at Nano Sun Abrad, with the inner vessel and its piping above the outer shell's bottom head"
description: "Redesigning supports, nozzles, and insulation of vacuum-insulated cryogenic tanks, guided by FloEFD models validated against boil-off measurements."
image: { path: /assets/img/projects/storage-tank-thermal-bridges/cover.webp, alt: "Cryogenic storage tank under construction at Nano Sun Abrad, with the inner vessel and its piping above the outer shell's bottom head" }
outputs:
  - { label: "Commercial product range (internal R&D)", url: "" }
---
## Motivation

Nano Sun Abrad builds double-walled tanks for liquid oxygen, liquid nitrogen, and liquid CO₂, with the insulation inside an evacuated annulus. The company wanted to upgrade these products to stay competitive. In such a tank, the weak points are often not the insulation itself. Supports, nozzles, bolts, and seams form solid paths across a very large temperature difference, and heat loss at a thermal bridge can be up to 50 times higher than through the insulation. Every watt that leaks in boils off stored liquid.

## Approach

The tanks ranged from 50-liter vessels to 20,000–44,000-liter tanks, vertical for storage and horizontal for transport, rated for 10 to 25 bar. Customers could choose the annulus insulation: multilayer insulation (MLI), perlite, or Layered Composite Insulation for Extreme Conditions (LCX), which I helped develop.

I first located thermal bridges on finished tanks with a thermal camera. I then built FloEFD models inside SolidWorks, with CAD in Solid Edge and SolidWorks. Depending on the question, I modeled the whole tank, a symmetric section, or a single detail such as one support leg, in both steady-state and transient runs. I used the models to compare design options: low-conductivity support materials and longer heat paths, redesigned nozzle necks, insulated bolts, and sealed or overlapped seams.

After construction, I checked each model against the real tank. I measured the boil-off rate by weighing, with a flow meter, and from the level drop over several days, then converted it into absorbed heat.

## Results

Simulated maximum and average temperatures agreed with measurements within 5 %. The heat-transfer coefficient, Nusselt number, and heat flux agreed within about 10–15 %. After the changes, thermal-camera images no longer showed the cold spots at the former thermal bridges. The measured reductions in heat leak are confidential company data. The work led to a range of tank products that the company manufactures and sells.

{% include figure.html src="/assets/img/projects/storage-tank-thermal-bridges/cross-section.webp" alt="Cross-section of a double-walled cryogenic tank showing the inner vessel, vacuum annulus, and outer shell" caption="Cross-section of a double-walled tank. The insulation sits in the evacuated annulus between the inner vessel and the outer shell." %}

{% include figure.html src="/assets/img/projects/storage-tank-thermal-bridges/support-detail.webp" alt="Photo of a support between the inner vessel and outer shell of a cryogenic tank" caption="Support detail. Supports like this one are the main solid heat paths into the cold vessel." %}

{% include figure.html src="/assets/img/projects/storage-tank-thermal-bridges/temperature-field.webp" alt="Simulated FloEFD temperature field around a tank support, with a colorbar in kelvin" caption="Simulated FloEFD temperature field used to compare design options at a thermal bridge." %}

{% include figure.html src="/assets/img/projects/storage-tank-thermal-bridges/temperature-cut.webp" alt="Simulated FloEFD cut plot through an internal tank support, with the bolts drawn as outlines and a colorbar in kelvin" caption="Simulated cut through the same support. The layered block and its bolts hold the inner vessel in place inside the vacuum annulus." %}

## My contribution

I was the only engineer in the R&D unit, and four engineers from production engineering worked under my supervision. I chose the insulation materials and designed the support structures. I ran the thermal-camera surveys, built and validated the simulation models, wrote the test procedures, and sometimes trained the installers.
