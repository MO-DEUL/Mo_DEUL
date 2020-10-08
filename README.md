# 모들 백엔드 개발

Backend files made with Django for Team Moduel

![Alt text](logo/logo1.png)

## Dockerfile<hr/>

The base image is python:3.8. Set Django version to 3.1 and other libraries(django-seed, django-filter, pillow.....) version is on requirements.txt.

    $ docker build -t backend-moduel:latest .
    $ docker run -d -p 8000:8000 backend-moduel

## Command <hr/>

### Run server without Docker

    pipenv shell -> python manage.py runserver

> if you need migrate

    python manage.py makemigrations -> python manage.py migrate

> if you want to join admin panel

    python manage.py createsuperuser

### Making FakeDB

> User DB

    python manage.py seed_users --number 원하는 수 만큼

> Houses DB

    python manage.py seed_houses --number 원하는 수 만큼

> House Type DB

    python manage.py seed_houseType

> Amenities DB

    python manage.py seed_amenity

> Facilities DB

    python manage.py seed_facility
