---
title: "Thermal Protection of a Battery-Powered Ladle Carrier at Mobarakeh Steel"
summary: "Sixteen FloEFD simulations of insulation, fans, and battery layout to keep batteries below 50 °C beside a molten-metal ladle."
group: industry
order: 2
featured: true
role: "Junior Engineer"
organization: "Pakan Atiye Nano Danesh Co. (PANDA)"
period: "2021 – 2022"
theme: heat-transfer-cfd
tools: [FloEFD, SolidWorks, CATIA]
cover: /assets/img/projects/mobarakeh-steel-heat-transfer/cover.webp
cover_alt: "Simulated temperature field of a battery-powered ladle carrier"
description: "Sixteen FloEFD simulations of insulation, fans, and battery layout to keep batteries below 50 °C beside a molten-metal ladle."
image: { path: /assets/img/projects/mobarakeh-steel-heat-transfer/cover.webp, alt: "Simulated temperature field of a battery-powered ladle carrier" }
outputs:
  - { label: "Technical report for Mobarakeh Steel Co. (not public)", url: "" }
---
## Motivation

At Mobarakeh Steel Co., a battery-powered vehicle runs on rails and carries a ladle of molten metal. The ladle's outer wall reaches about 400 °C, and the battery compartments sit just below it. Heat reaches the batteries by conduction through the ladle's support legs and by radiation. Too much heat lowers battery performance and can melt casings or cause acid leaks. The client asked us to keep battery surfaces below 50 °C, with very little space for insulation.

## Approach

I ran 16 FloEFD cases, with geometry built in CATIA and SolidWorks. The cases moved step by step from a bare baseline to thin aerogel blankets, cooling fans, new battery layouts, and molten metal spilled on the rails or under the vehicle. The inputs came from the client's operating data, and we also tested worst-case conditions such as hot summer air. Most runs were steady-state, which is conservative, because the real vehicle keeps moving.

The vehicle has two identical, symmetric battery compartments. I used this symmetry to cut the computing load, and in some runs I gave the two compartments different conditions to compare designs side by side. Meshes stayed coarse to keep run times manageable.

## Results

The support legs were the main heat path, and the closed compartment trapped hot air. Both insulation and forced airflow were needed; neither was enough alone. Insulating only half of the carrier area gave almost the same result as full coverage, which saves aerogel. With aerogel insulation and two fans, the simulated average battery temperature stayed below 40 °C. The spill cases showed where extra shielding was needed: the compartment floor, the backs of the sweepers, and the underside of the vehicle.

PANDA's recommendations were implemented on the vehicle, and the client gave positive feedback.

{% include figure.html src="/assets/img/projects/mobarakeh-steel-heat-transfer/baseline.webp" alt="Simulated temperature field of the ladle carrier without insulation, with colorbar" caption="Simulated baseline case without insulation. Heat enters mainly through the ladle's support legs." %}

{% include figure.html src="/assets/img/projects/mobarakeh-steel-heat-transfer/baseline-underside.webp" alt="Simulated temperature field of the ladle carrier's frame seen from below, without insulation, with a colorbar in °C" caption="Simulated baseline case seen from below. The warmest parts of the frame lie under the ladle." %}

{% include figure.html src="/assets/img/projects/mobarakeh-steel-heat-transfer/insulation-two-fans.webp" alt="Simulated air-flow trajectories around a block of battery modules, colored by air temperature, with a colorbar in °C" caption="Aerogel insulation with two fans, showing simulated air paths around the battery modules. The simulated average battery temperature stays below 40 °C." %}

## My contribution

I ran all 16 simulation cases and contributed to the decisions on battery layout and air paths. I co-drafted the recommendations with Dr. Hasan Bargozin, the project manager and manager of PANDA, and took part in writing the technical report.
