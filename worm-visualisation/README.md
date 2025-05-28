# Worm Propagation Visualization Project

## Overview

This project simulates the propagation of two classic computer worms — **Code Red** and a custom worm named **Voyager** — through a virtual network of vulnerable machines. The environment is segmented into subnetworks with controlled bridges, and propagation is tracked and visualized in real-time.

---

## Features

- Simulated worm propagation based on real attack vectors
- Network segmentation with cross-network bridging
- Real-time infection monitoring from logs
- Interactive visualization using NetworkX and Matplotlib
- DFS visualization to trace propagation path
- Reset functionality to clean infections and restart

---

## Project Structure

/
├── vagrant/ # Vagrant setup for VM provisioning
├── logs/ # Log directory for infection events
│ ├── code_red.log
│ └── voyager.log
├── visualizer.py # Main visualization script. Includes DFS visualization
├── monitoring.py # Monitors logs and prints infection status
── codeRed.py # Simulation of code red worm
── voyager.py # Simulation of voyager worm 
├── reset.py # Clears logs and resets infection state
├── requirements.txt # Python dependencies
└── README.md # This file

##Quick Demo Video: [worm] (https://studio.youtube.com/video/4hoI67Z1hKo/edit)
