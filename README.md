# Django Playground

This is a little playground to experiment with Docker. The docker-compose.yml creates three containers that include a nginx reverse proxy server, a django app and a postgres db. Containers are linked via a custom bridge network.

`app` and `http` share the `frontend` network. `db` and `app` share the `backend` network. `app` exposes port 8000 via gunicorn. nginx proxies `app:8000` (app resolved by docker) and listen to port 80. `http` binds nginx port 80 to host's localhost:8080.


## Some commands

- Run the docker project `docker-compose up`
- Enter a container terminal: `docker exec -it container_id /bin/bash`
- Run Django shell `docker exec -it container_id python manage.py shell`
- Stop and delete all containers `[sudo] ./tidydocker`
- Services logs `docker-compose logs http`

## References & Notes

### Nginx

- Docker image <https://hub.docker.com/_/nginx/> or <https://store.docker.com/images/nginx>
- nginx.conf <http://nginx.org/en/docs/beginners_guide.html>
- nginx.conf + guinicorn <http://docs.gunicorn.org/en/latest/deploy.html>

### Gunicorn

- Docs <http://docs.gunicorn.org/>

### Python

- Python and Docker <https://docs.docker.com/samples/library/python/>

### Postgres

- Django and Docker <https://docs.docker.com/compose/django/#connect-the-database>

### Django

- <https://docs.djangoproject.com/en/2.0/intro/tutorial01/>
- <https://docs.djangoproject.com/en/2.0/intro/tutorial02/>

### Docker, Docker compose, Gunicorn, Nginx, Pstgres, Django and Python

- Used a full version Python image with psycopg2
- Added postgres service environment variables to settings.py.
- Used custom bridge network between containers <https://docs.docker.com/network/network-tutorial-standalone/> and <https://docs.docker.com/compose/networking/#specify-custom-networks>
- Specified two networks, frontend and backend, only app attached to both
- Create a new project: docker-compose run app django-admin.py startproject name_of_project
