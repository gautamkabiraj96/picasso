# Database

## Windows:

cd \Postgres\bin
.\pg_ctl.exe restart -D G:\Programs\Postgres\data

### use postgres pass instead of windows pass

PS G:\Programs\Postgres\bin> .\psql -U <dbuser> -h localhost
Password for user <dbuser>:

## remove migrations

find . -path "_/migrations/_.py" -not -name "**init**.py" -delete
find . -path "_/migrations/_.pyc" -delete

## Mac:

brew services start postgresql

# API

## Deps

pip install psycopg2 psycopg2-binary django djangorestframework

## Start server

python3 manage.py runserver

## Activate venv

### Mac:

source ../venv/bin/activate

### Windows:

.\Scripts\activate

## Migrations

python manage.py makemigrations
python manage.py migrate
