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

Start the server
 >py manage.py runserver

In another terminal, run celery
 >celery -A upload_image worker -l info --pool=solo
