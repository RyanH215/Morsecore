# Morsecore
**A cyberdeck-ready, Raspberry Pi-based Morse code communication system for off-grid and SHTF scenarios.**

MorseCore turns your Raspberry Pi 4B and Raspberry Pi Pico into a complete Morse code station — capable of transmitting real CW signals over the air and decoding received Morse via microphone input. Built for resilience, portability, and zero-dependency operation.

## Table of Contents

- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Transmitter Wiring Diagram (Keying)](#transmitter-wiring-diagram-keying)
- [Legal Notice](#legal-notice)
- [License](#license)
- [Author](#author)
- [Tags](#tags)

## Features

- **CW Transmission**: Type a message and transmit it via real RF using a keyed transmitter.
- **Text-to-Morse Encoder**: Converts typed messages into accurate Morse code.
- **Pico-Based Keyer**: Uses a Raspberry Pi Pico to key a CW transmitter via GPIO.
- **Audio Sidetone**: Optional buzzer or speaker feedback when transmitting.
- **Mic-Based Decoder**: Listen to Morse audio (via mic) and decode it into readable text.
- **Waveform Visualizer**: View real-time audio input for debugging or learning.
- **Cross-Platform GUI**: Clean Tkinter interface for Linux (Pi OS) and Windows.
- **USB & Bluetooth Keyboard Support**: Flexible input options for cyberdeck or remote use.

## Hardware Requirements

- **Raspberry Pi 4B** – Main controller + GUI
- **Raspberry Pi Pico** – Morse code keyer (via GPIO)
- **CW Transmitter (e.g., Pixie)** – Broadcasts RF signal
- **NPN Transistor (e.g., 2N2222)** – Keys transmitter
- **Buzzer or small speaker** – Sidetone (optional)
- **USB or Bluetooth keyboard** – Message input
- **Microphone (USB or analog)** – Decode incoming Morse
- **Longwire or dipole antenna** – RF signal transmission

## Software Requirements

Install Python packages (on the Pi or Windows):

```bash
pip install pyserial pyaudio numpy matplotlib
```

## Project Structure

```
morsecore/
├── main.py               # Central control GUI
├── morse_encoder.py      # Text → Morse conversion
├── morse_transmit.py     # Send Morse over serial to Pico
├── morse_decoder.py      # Mic-based Morse audio decoding
├── visualizer.py         # Audio waveform display
├── pico_keyer.py         # MicroPython CW keyer (load to Pico)
```

## Usage

1. Flash the `pico_keyer.py` script to your Raspberry Pi Pico using [Thonny](https://thonny.org/).
2. Connect the Pico’s GPIO pin (e.g., GPIO 15) to the **key input** of your CW transmitter using a transistor circuit.
3. On the Pi 4B, run:

```bash
python3 main.py
```

4. Type your message, view the Morse preview, and click **Transmit**.
5. Listen for side-tone feedback or monitor the waveform.
6. For decoding, run:

```bash
python3 morse_decoder.py
```

to decode audible Morse signals received via microphone.

## Transmitter Wiring Diagram (Keying)

```
Pico GPIO 15 ──┬──> 1kΩ resistor ──> Transistor Base
               │
          Collector ──> TX key input
          Emitter ──> GND (common with TX and Pico)
```

## Legal Notice

This project includes the ability to key and transmit real radio signals. In most countries (including the U.S.), transmitting outside of license-exempt bands without a proper amateur radio license is illegal, except during emergency scenarios.

Use responsibly. In a SHTF situation, it may be the only signal that gets through.

## License

This project is open-source and licensed under the [MIT License](LICENSE).

## Author

Ryan H.  
Inspired by off-grid resilience, amateur radio ops, and the spirit of analog comms.

## Tags

`raspberry-pi` `morse-code` `cw` `ham-radio` `cyberdeck` `shtf` `off-grid` `radio` `micropython` `transmitter` `field-ready`
