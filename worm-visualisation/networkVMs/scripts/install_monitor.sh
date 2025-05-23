#!/bin/bash
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install flask colorama
echo "Monitoring tools installed"

mkdir -p /vagrant/logs
touch /vagrant/logs/code_red.log
touch /vagrant/logs/voyager.log

chmod +x /vagrant/scripts/monitor.py

cd /simulation
nohup python3 codeRed.py > /vagrant/logs/code_red_simulation.log 2>&1 &
nohup python3 voyager.py > /vagrant/logs/voyager_simulation.log 2>&1 &
echo "🚀 Worm simulations started."

nohup python3 /vagrant/scripts/monitor.py > /vagrant/logs/monitor_output.log 2>&1 &
echo "Monitor script started in background. Log: /vagrant/logs/monitor_output.log"