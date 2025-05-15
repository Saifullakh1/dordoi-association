How to install application for the first time

From terminal run command python3 -m venv env
Then run source env/bin/activate
Then run pip install -r requirements.txt In case of error due to backports.zoneinfo, you may comment out it from requirements.txt and then rerun previous command

How to run app on your local machine

Run source env/bin/activate
Run ./manage.py runserver you should have running app in your machine
