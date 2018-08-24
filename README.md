# QIIME 2 Library

## Development Quickstart

```
conda create -n library
source activate library
conda install pip
pip install -r requirements/local.txt
createdb qiime2-library
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Produdction Environment Variables

- `ALLOWED_HOSTS`
- `DATABASE_URL`
- `DISCOURSE_SSO_SECRET`
- `DJANGO_SETTINGS_MODULE`
- `SECRET_KEY`

## Misc

- `openssl rand -base64 66 | tr -d '\n'`
