How can I start the project?
===============
Create a virtual environment and activate it:
 >py -m venv venv
 >
 >venv\Scripts\activate
  
Install all necessary dependencies on the virtual machine
 >pip install django
 >
 >pip install pyuploadcare
 >
 >pip install celery

Run celery in this terminal
 >celery -A upload_image worker -l info --pool=solo

In another terminal, start the server
 >py manage.py runserver
