## Start server

python3 manage.py runserver

## Activate venv

source ../venv/bin/activate

## Run migrations

python3 manage.py migrate

## Create migrations

python3 manage.py makemigrations <app_name>

## Deps for PostGres

pip install psycopg2  
pip install psycopg2-binary
