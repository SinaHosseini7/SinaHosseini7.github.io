---
title: "PicoPhone: A DIY Mobile Phone on Raspberry Pi Pico 2"
summary: "A from-scratch mobile phone on a Raspberry Pi Pico 2 and SIM800C modem, with C firmware; display, touch, and SMS work so far."
group: personal
order: 1
featured: false
role: "Designer and developer"
organization: "Personal project"
period: "2025 – present"
theme: ""
tools: [C, Raspberry Pi Pico 2, SIM800C, Electronics prototyping]
cover: /assets/img/projects/picophone/cover.webp
cover_alt: "Design block diagram of PicoPhone around a Raspberry Pi Pico 2"
description: "A from-scratch mobile phone on a Raspberry Pi Pico 2 and SIM800C modem, with C firmware; display, touch, and SMS work so far."
image: { path: /assets/img/projects/picophone/cover.webp, alt: "Design block diagram of PicoPhone around a Raspberry Pi Pico 2" }
outputs:
  - { label: "Code (GitHub, in progress)", url: "https://github.com/sinahosseini7/picophone" }
---
## Motivation

I started PicoPhone to learn electronics from the basics. A phone is a demanding teacher: it needs a cellular modem, a touch display, a battery and charger, and audio, all run by a microcontroller with no radio and no operating system of its own. PicoPhone is built around a Raspberry Pi Pico 2 and a SIM800C 2G GSM module, and it is still in progress.

## Approach

I write the firmware in C and use Claude, Anthropic's AI model, to speed up coding and to organize the design specification. The specification records each design decision with its reasoning and marks values that still need checking against a datasheet or on the bench. An AI-assisted design review with Claude Opus found errors in my early wiring, battery, and charging choices, and I corrected them. Three decisions show the kind of problems involved.

**Supply droop during transmit bursts.** The SIM800C draws up to about 2 A for 577 µs in every 4.615 ms GSM frame, and its supply must stay above 3.0 V. From ΔV = I·t / C, 1,100 µF gives a calculated drop of about 1.05 V, which is too much. With 2,200 µF the drop is about 0.52 V, and with about 0.2 V of resistive drop added, the calculated minimum supply from a 4.0 V start is about 3.28 V.

**One SPI bus for display and touch.** The display and touch controller share a bus. Display writes run at up to 25 MHz and touch reads at 2 MHz or less, so the clock changes per transaction. Before a touch read, the firmware waits until the DMA transfer has finished and the SPI peripheral's busy flag has cleared. Waiting for DMA alone would cut off the last pixels and corrupt the touch reading.

**The SMS prompt.** To send an SMS, the module answers with a `> ` prompt that has no line ending. A line-based parser would wait forever, so the command handler scans the incoming bytes for `>` directly.

## Results

So far, I have working parts rather than a finished phone. My display driver, written from the datasheet, initializes the display and reads touch input. Through the SIM800C, I can send and receive SMS in text mode, including Unicode and multipart messages. The parts are not yet integrated on one breadboard, and there is no PCB yet. All numbers above are design calculations, not measurements.

{% include figure.html src="/assets/img/projects/picophone/block-diagram.webp" alt="Block diagram: Pico 2 connected to the SIM800C by UART, to the display and touch controller by a shared SPI bus, to the charger by I2C, and to an audio switch" caption="System block diagram (design)." %}

{% include figure.html src="/assets/img/projects/picophone/power-tree.webp" alt="Power tree from USB-C through the BQ25895 charger to the modem's capacitor bank, the 3.3 V rails, and the RTC supercapacitor" caption="Power tree (design). The 2,200 µF bank at the modem supply comes from the droop calculation above." %}

{% include figure.html src="/assets/img/projects/picophone/breadboard.webp" alt="Raspberry Pi Pico 2 on a breadboard, wired with jumper wires to a SIM800C modem board held in one hand" caption="The Pico 2 wired to the SIM800C module on a breadboard. The parts are tested separately and are not yet integrated." %}

## My contribution

PicoPhone is my own project. I do the wiring and testing and write the firmware, with the AI support described above.
