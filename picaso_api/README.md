# App
## Start server

python3 manage.py runserver

## Activate venv

source ../venv/bin/activate

## Run migrations

python3 manage.py migrate

## Create migrations

python3 manage.py makemigrations <app_name>

## Deps

pip install psycopg2 psycopg2-binary django djangorestframework

# Database

## windows:
 cd \Postgres\bin
 .\pg_ctl.exe restart -D G:\Programs\Postgres\data

### use postgres pass instead of windows pass
PS G:\Programs\Postgres\bin> .\psql -U postgres -h localhost
Password for user postgres:

 ## mac:
brew services start postgresql
