#!/usr/bin/python
import os
os.system("apt-get install python-django python-jinja2 python-pip")
os.system("pip install facebook-sdk pytz")
os.system("mkdir $HOME/RideBuddy")
os.system("cp ./* $HOME/RideBuddy -r")
os.system("touch /usr/bin/ridebuddy")
command = "cd " + os.getenv("HOME") + "/RideBuddy/carpoolsen && python manage.py syncdb && python manage.py runserver"
os.system("echo \"" + command + "\" > /usr/bin/ridebuddy")
os.system("chmod +x /usr/bin/ridebuddy")
f = open(os.getenv("HOME") + "/RideBuddy/carpoolsen/paths.py","w")
f.write("cpspath = '" + os.getenv("HOME") + "/RideBuddy/'")
f.close()
os.system("sudo chmod 777 " + os.getenv("HOME") + "/RideBuddy/ -R")
print "Installation Finished. run 'ridebuddy' to start server, and then go to http://localhost:8000/"