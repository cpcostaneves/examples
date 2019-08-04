# Django

## Start server

Enter virtual env, install dependencies, run server
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver 0.0.0.0:8000
```

Access Admin interface
- http://127.0.0.1:8000/admin/
- user: admin
- pass: localdev

API (GET / POST / PATCH / DELETE):
- http://127.0.0.1:8000/persons/


## Refs

Settings
https://mitchel.me/2016/settings-management-in-django/

Env
https://github.com/joke2k/django-environ
https://django-environ.readthedocs.io/en/latest/
https://pypi.org/project/django-environ/

Permissions
https://www.django-rest-framework.org/api-guide/authentication/
https://www.django-rest-framework.org/api-guide/permissions/
https://jpadilla.github.io/django-rest-framework-oauth/permissions/
https://jpadilla.github.io/django-rest-framework-oauth/authentication/

