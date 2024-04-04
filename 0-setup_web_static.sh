#!/usr/bin/env bash
# sets up the web server for deployment of web static

#install nginx if it doesn't exist
apt-get -y update
apt-get -y install nginx

# create required directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# store test html file content in a variable
index='<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8" />\n\t<title>Hello, world!</title>\n\t<meta name="viewport" content="width=device-width,initial-scale=1" />\n\t<meta name="description" content="" />\n\t<link rel="icon" href="favicon.png">\n</head>\n<body>\n\t<h1>Hello, world!</h1>\n</body>\n</html>'

# save the content to a file named index.html
echo -e ${index} > /data/web_static/releases/test/index.html

# create a symbolic link to the test directory
ln -sf /data/web_static/current /data/web_static/releases/test/

# change ownership of /data directory to user ubuntu
chown -R ubuntu /data/
chgrp -R ubuntu /data/

new_config="\t}\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;"

sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf

# configures nginx 
sed -i "\/^\\t\\ttry_files \$uri \$uri\/ \404\;/r $new_config"

service nginx start
