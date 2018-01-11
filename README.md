# Django Playground

This is a personal playground to experiment with python and Django + PosgreSQL wraped up with Docker.

## Components

- Python and Docker <https://docs.docker.com/samples/library/python/>
- Django and Docker <https://docs.docker.com/compose/django/#connect-the-database>
- PostgreSQL db and psycopg2 (package to use PostgreSQL)
- (Does not include server)

## Usage

- Run a docker project `docker-compose up`
- Enter a container terminal: `docker exec -it container_id bash`
- Create a project via compose `docker-compose run app django-admin.py startproject play_project`
- Run Django shell `docker exec -it container_id python manage.py shell`
- Start server `python manage.py runserver 0.0.0.0:8000`

## Docker/Python/Django Notes

Used a full version Python image as Alpine image causing trouble with psycopg2 but should modify an Alpine image in the future.

Added postgres service environment variables to settings.py.

## Tuts Links

- <https://docs.djangoproject.com/en/2.0/intro/tutorial01/>
- <https://docs.djangoproject.com/en/2.0/intro/tutorial02/>