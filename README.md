## How to install application for the first time

1. From terminal run command `python3 -m venv env`
2. Then run `source env/bin/activate`
3. Then run `pip install -r requirements.txt`
   In case of error due to `backports.zoneinfo`, you may comment out it from requirements.txt and then rerun previous command

## How to run app on your local machine

1. Run `source env/bin/activate`
2. Run `./manage.py runserver` you should have running app in your machine
