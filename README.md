# django_animal
Web application for database management via rest-api

## Getting started

1. get the code from the repository
```
https://github.com/leondav1/django_animal.git
```

2. create a virtual environment, activate it and retrieve all needed python packages
```
cd path/to/django_animal
python3 -m venv name_venv
source name_venv/bin/activate (for Linux)
name_venv\Scripts\activate.bat (for windows)
pip install -r requirements.txt
```

3. create superuser
```
python manage.py createsuperuser
```

4. start the server
```
python manage.py runserver
```

## swagger
```
access to path: 127.0.0.1:8000/swagger or your_host/swagger
access to path: 127.0.0.1:8000/redoc or your_host/redoc
```
