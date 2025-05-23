#!/bin/bash
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install flask colorama
echo "Monitoring tools installed"

mkdir -p /vagrant/logs
touch code_red.log
touch voyager.log

chmod +x /vagrant/scripts/monitor.py

nohup python3 /vagrant/scripts/monitor.py > /vagrant/logs/monitor_output.log 2>&1 &
echo "Monitor script started in background. Log: /vagrant/logs/monitor_output.log"