# TECHIN515 Lab 4: Smart Gesture Wand

## Overview

This repository contains all source code, design files, data, and documentation for our smart gesture wand, created for TECHIN 515 Spring 2025 Lab 4.

The wand utilizes an IMU (e.g., MPU6050) to capture gesture motion data, processes it using a model trained via Edge Impulse, and is enclosed in a custom-designed casing with integrated battery and board stabilization.

## Repository Structure

```
├── src/
│   ├── sketches/               # Arduino sketches with comments and Edge Impulse deployment code
│   ├── python-scripts/         # Python scripts for data collection
│   └── dataset/                # Collected raw .csv data
│
├── docs/
│   └── report.pdf              # Final self-contained report
│
├── media/
│   └── demo.mp4                # Demo video (under 3 minutes)
│
├── enclosure/
│   ├── final-enclosure-images/ # Photos of the assembled wand
│   └── notes.md                # Materials, battery info, design considerations
│
├── README.md
└── .gitignore
```

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SyHilichurl/515lab5.git
cd 515lab5
```

### 2. Hardware Requirements

- **Microcontroller:** Seeed XIAO RP2040 / ESP32
- **Sensor:** MPU6050 (IMU)
- **Battery:** Rechargeable Li-ion (3.7V)
- **Additional Components:** Breadboard, jumper wires, USB cable

### 3. Software Requirements

- **Arduino IDE** 
- **Edge Impulse CLI** 
- **Python**

### 4. Installation Steps

#### a. Arduino Sketches

1. Navigate to the `src/sketches/` directory.
2. Open the desired `.ino` file in the Arduino IDE.
3. Connect your microcontroller via USB.
4. Select the appropriate board and port in the Arduino IDE.
5. Import library using the `.zip` file.
6. Upload the sketch to the microcontroller.

#### b. Python Scripts

1. Navigate to the `src/python-scripts/` directory.
2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the data collection script:

   ```bash
   python collect_data.py
   ```

#### c. Edge Impulse Deployment

1. Use the collected data in `src/dataset/` to train a model on Edge Impulse.
2. Export the trained model as an Arduino library.
3. Replace the existing library in `src/sketches/` with the new one.
4. Re-upload the sketch to the microcontroller.

### 5. Enclosure Fabrication

1. Use the design files in the `enclosure/` directory to fabricate the casing using a laser cutter.
2. Assemble the enclosure as per the instructions in `enclosure/notes.md`.
3. Ensure all components, including the microcontroller and battery, are securely mounted.

## Report

A comprehensive report detailing the project's objectives, design decisions, data collection process, model architecture, performance metrics, and challenges faced is available at [`docs/report.pdf`](docs/report.pdf).

## Demo Video

A demonstration of the smart gesture wand's functionality can be viewed at [`media/demo.mp4`](media/demo.mp4).

## License

This project is open-source and available under the [MIT License](LICENSE).
