---
title: "Python Modules for a Darcy-Flow Reservoir Simulator"
summary: "Python modules for input, streamline visualization, field plotting, and reporting in a reservoir simulator used to compare well locations."
group: software
order: 1
featured: false
role: "Python Developer"
organization: "Ahmadi Roshan Research Project, Iran's National Elites Foundation"
period: "2020 – 2022"
theme: heat-transfer-cfd
tools: [Python, NumPy, Matplotlib, VTK]
cover: /assets/img/projects/flow-simulation-software/cover.webp
cover_alt: "Simulated 3D streamlines in a 13-well reservoir test case, colored by injector well"
description: "Python modules for input, streamline visualization, field plotting, and reporting in a reservoir simulator used to compare well locations."
image: { path: /assets/img/projects/flow-simulation-software/cover.webp, alt: "Simulated 3D streamlines in a 13-well reservoir test case, colored by injector well" }
outputs:
  - { label: "Proprietary software (code not public)", url: "" }
---
## Motivation

An oil reservoir is produced through extraction wells, with water or gas pumped in through injection wells. Where a new well goes affects how much oil the field finally recovers. The Ahmadi Roshan Research Project, under Iran's National Elites Foundation, was building simulation software to find good locations for new wells before drilling. The program places students in research teams led by a professor. I applied with proposals for five projects, was interviewed for this one, and was selected while still an undergraduate.

## Approach

The simulator models flow through porous rock with Darcy's law. The team had about 15 members and used data from a real reservoir as the basis of the problem. I worked remotely and wrote Python modules both inside the simulator and around its results:

- input reading;
- streamline visualization, showing flow paths, time of flight, and swept regions;
- plotting of pressure and saturation fields;
- post-processing and report export.

I used NumPy for the numerical work, Matplotlib for plots, and VTK for visualization. I kept my code under version control with Git.

## Results

The team checked the software against data from the reservoir and benchmarked it against StreamSim, a commercial streamline simulator. The final software belongs to the project and is not open source, so the figures below show only test and synthetic cases. For me, the project meant two years of writing numerical Python inside a code base shared by a team.

{% include figure.html src="/assets/img/projects/flow-simulation-software/streamlines.webp" alt="Simulated 3D streamlines in a 13-well test case, colored by mean velocity, with a colorbar in m/day" caption="Simulated streamlines in a test case with four injectors and nine producers, colored by mean velocity." %}

{% include figure.html src="/assets/img/projects/flow-simulation-software/streamlines-5spot.webp" alt="Simulated 3D streamlines in a five-spot test case, colored by depth, with a colorbar in meters" caption="Simulated streamlines in a five-spot test case, with one injector at the center and four producers at the corners." %}

{% include figure.html src="/assets/img/projects/flow-simulation-software/well-allocation.webp" src_dark="/assets/img/projects/flow-simulation-software/well-allocation-dark.webp" alt="Plan view of the 13-well test case with lines from each injector to the producers it supplies, labeled with allocation percentages" caption="Simulated well allocation factors for the same case: the share of each injector's rate that reaches each producer." %}

## My contribution

I wrote the modules listed above. Dr. Majid Siavashi and Dr. Rohaldin Miri led the team: they set the tasks, reviewed the code, and managed the team. I also mentored three to five junior members in Python and numerical methods through code reviews, short tutorials, and pair programming.
