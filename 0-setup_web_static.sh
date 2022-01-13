#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# Create folders and file html
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
touch /data/web_static/releases/test/index.html
echo "Welcome!" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content 
sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

# Restart Nginx after updating the configuration
service nginx restart
