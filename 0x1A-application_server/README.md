---

# Project: Tasks

## Introduction
This project involves setting up development and production environments for an AirBnB clone using Flask, Gunicorn, and Nginx. The project is divided into several tasks, each focusing on specific configurations and setups. Follow the instructions below to complete each task.

## Task 0: Set up development with Python
### Requirements
- Ensure that task #3 of your SSH project is completed for web-01.
- Install the net-tools package on your server: `sudo apt install -y net-tools`
- Git clone your AirBnB_clone_v2 repository on your web-01 server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.

### Example
Window 1:
```
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
```

## Task 1: Set up production with Gunicorn
### Requirements
- Install Gunicorn and any other libraries required by your application.
- Serve the same content from the same route as in Task 0 using Gunicorn on port 5000.

### Example
Terminal 1:
```
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
```

## Task 2: Serve a page with Nginx
### Requirements
- Configure Nginx to serve your page from the route `/airbnb-onepage/`.
- Nginx should proxy requests to the process listening on port 5000.

### Notes
- Ensure your application server is running on port 5000.

## Task 3: Add a route with query parameters
### Requirements
- Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance listening on port 5001.

### Tips
- Utilize Nginx reverse proxy and location blocks for this configuration.

## Task 4: Serve your AirBnB clone
### Requirements
- Serve content from `web_dynamic/2-hbnb.py` on port 5003 using Gunicorn.
- Configure Nginx to serve static assets found in `web_dynamic/static/`.
- Ensure proper configuration of `web_dynamic/static/scripts/2-hbnb.js` with the correct IP.

## Task 5: Deploy it!
### Advanced
- Write a systemd script to start a Gunicorn process serving content from `web_dynamic/2-hbnb.py` on port 5003.
- The Gunicorn process should spawn 3 worker processes and log errors in `/tmp/airbnb-error.log`.

## Task 6: No service interruption
### Advanced
- Write a Bash script to reload Gunicorn gracefully, allowing for updates without downtime.

---
