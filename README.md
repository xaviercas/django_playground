# Django Playground

This is a personal playground to experiment with python and Django + PosgreSQL wraped up with Docker.

## Components

- Python and Docker <https://docs.docker.com/samples/library/python/>
- Django and Docker <https://docs.docker.com/compose/django/#connect-the-database>
- PostgreSQL db and psycopg2 (package to use PostgreSQL)
- (Does not include server)

## Usage

- Create a project `docker-compose run app django-admin.py startproject play_project` then edit your settings.py and `docker-compose up`
- Run a project `docker-compose up`
- Enter a container terminal (eg migrations): `docker exec -it container_id bash`

## Tuts Links

- <https://docs.djangoproject.com/en/2.0/intro/tutorial01/>
- <https://docs.djangoproject.com/en/2.0/intro/tutorial02/>

## Docker Notes

- Used a full version Python image as Alpine image causing trouble with psycopg2 but should modify an Alpine image in the future.
- In compose file ensure path includes current project name: `/code/play_project/manage.py` in `python /code/play_project/manage.py runserver 0.0.0.0:8000`
- I have changed the working directory to the project path in compose.
- I have added the db environment variables and modified settings.py

## Python / Django Notes

- `if __name__ == "__main__":` in manage.py: interpreter gives the __name__ the value of __main__ when it executes the file direcly, id not as an import. So prevents manage.pyto be imported, id the code under condition statement will execute.
- app vs project: project has many apps & apps can be shared between projects