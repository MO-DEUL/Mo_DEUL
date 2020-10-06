# 모들 백엔드 개발

## Command

### Run server without Docker

> > pipenv shell -> python manage.py runserver

#### if you need migrate

> > python manage.py makemigrations -> python manage.py migrate

#### if you want to join admin panel

> > python manage.py createsuperuser

### Making FakeDB

> > User DB: python manage.py seed_users --number {원하는 수 만큼}
