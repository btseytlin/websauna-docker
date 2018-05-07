# Dockerized Websauna application

This is the application from [cookiecutter-websauna-app](https://github.com/websauna/cookiecutter-websauna-app), running in Docker containers.

Rationale: Websauna has external dependencies (Postgres, Redis) which are easier managed using docker.


## Running
Requires `docker` and `docker-compose`
```
docker-compose up
```
Then access the app at `http://localhost:80`

## Developing
Bash into container:
```
docker-compose run --rm --service-ports app bash
```
Run `ws-*` commands as usual.

## Env variables
`POSTGRES_PASSWORD`
`POSTGRES_USER`
`POSTGRES_DB`
`SQLALCHEMY_DATABASE_URI` - postgres credentials

`CREATE_DEFAULT_USER` - if `true` creates default user on startup

`APP_DEFAULT_USER`, `APP_DEFAULT_PASSWORD` - default user credentials
