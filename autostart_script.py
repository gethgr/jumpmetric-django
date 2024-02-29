import os
import venv

startproject_name=input("give name for start project: ")
app_name=input("give name for app: ")

os.system(f""" python3 -m venv venv; 
              source venv/bin/activate;
              pip install django ; 
              django-admin startproject {startproject_name} .; 
              pip freeze > requirements.txt;
              python manage.py startapp {app_name};
              touch {app_name}/urls.py;
              python manage.py makemigrations;
              python manage.py migrate;
              
              
             """)
settings_object = open(startproject_name + '/settings.py', 'r')
filedata = settings_object.read()
filedata = filedata.replace("INSTALLED_APPS = [", f"INSTALLED_APPS = [\n    '{app_name}.apps.{app_name.capitalize()}Config', ")
settings_object.close()

settings_object = open(startproject_name + '/settings.py', 'w')
settings_object.write(filedata)
settings_object.close() 







