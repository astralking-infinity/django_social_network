# Blabber
A very simple social media application built with Django.

## Requirements
- python3
- pip

## Usage
```
$ git clone https://github.com/astralking-infinity/django_social_network
$ cd django_social_network
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## Configuration
- `SECRET_KEY` (environment variable): falls back to an insecure development key. Set your own before any deployment.
- The SQLite database (`db.sqlite3`) and uploaded files (`media/`) are not tracked; `migrate` creates the database.
