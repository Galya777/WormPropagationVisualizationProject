#!/bin/bash
sudo apt update
sudo apt install -y apache2
echo "Vulnerable Web Server Ready" | sudo tee /var/www/html/index.html
sudo ufw allow 80