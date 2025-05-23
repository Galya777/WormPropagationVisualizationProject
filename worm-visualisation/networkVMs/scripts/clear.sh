#!/bin/bash
sudo apt update && apt upgrade -y

cd /simulation
nohup python3 reset.py