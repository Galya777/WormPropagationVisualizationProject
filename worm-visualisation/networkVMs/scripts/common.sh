#!/bin/bash
sudo apt update && apt upgrade -y

# Install useful tools
sudo apt install -y python3 python3-pip git vim net-tools curl nmap wget

# Create directories
sudo mkdir -p /opt/wormlab/
sudo mkdir -p /vagrant/logs/

sudo useradd -m -s /bin/bash wormuser

sudo chmod -R 755 /opt/wormlab/

# Забраняваме изходящ достъп извън вътрешната мрежа
sudo iptables -A OUTPUT -d 0.0.0.0/0 -j DROP

# Позволяваме трафик САМО в private мрежата
sudo iptables -I OUTPUT -d 192.168.0.0/16 -j ACCEPT
