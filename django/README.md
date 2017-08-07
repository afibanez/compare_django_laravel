# Django README

## Installation
Its highly recomanable to install all python packages in a virtualenv:
```bash
virtualenv -p /usr/bin/python3 .venv
source .venv/bin/activate
```

With the virtualenv active, install all python dependences:
```bash
pip install -r requirements.txt
```

### First time kick off (not needed with the sqlite)
Execute migrations and create a super user
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Execution
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` to enter the Django Admin.
If you are using the provided sqlite:
- User: admin
- Pass: noworries

