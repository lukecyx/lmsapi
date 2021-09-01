# LMSAPI v1

## Project Status

WIP (Work in Progress).

## Project Aim

An API that serves as a backend API for a library/book store.

## Ratioanle

Acts as a playground for developing with Django.

Created for learning purposes with no real world use case.

## Requirements

- [Docker][2]
- [Poetry][3]

[2]: https://www.docker.com/
[3]: https://python-poetry.org/

## Setup with Docker (locally)

1. Run `./scripts/docker/docker-initial-setup.sh`

### Alternatively:

1. Build the project: `docker-compose up -d --build`. The project should now be running.
2. Run the migrations: `docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput`
3. Collect the static: `docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear`
4. Access the local server [lms.local](http://lms.local/)
5. View the logs with `docker-compose logs -f`

## Setup and Running Locally (without Docker, locally)

### Deprecated, won't work after the switch to Docker. (See Setup with Docker instead)

1. Ensure that your preferred db is installed (I've used Postgress for this project).
2. Install nginx.
3. Clone this project.
4. cd into project folder `lms-api`, if not there already.
5. Edit `lms_api/settings/base.py` with your database connection.
6. Create `secrets.json` in top level of the proejct and provide your secret key and your database password.
7. Activate the virutal environment `source venv/bin/active`.
8. Run the migrations for the database:
   i. `./manage.py makemigrations`.
   ii. `./manage.py migrate`.
9. Run `./setup-local.sh` as root.
10. Restart Nginx `sudo systemctl restart nginx`.

Note:

- As part of `./setup-local` the projects hostname (`lms.local/`) will be appended into your `/etc/hosts` file.
- `./setup-local` will also symlink `lms_nginx.conf` into `/etc/nginx/sites-enabled/` as `lms_nginx.conf`.

## Running Locally

### Deprecated. See Setup With Docker.

1. Run `./run-local.sh` from top level of the project.
2. Access API at `http://lms.local/api/v1/foo/bar/baz/`.

## Viewing the Projects Documentation

The project is documented using Mkdocs.
To view the docs:

1. cd into the top level of the project.
2. Run `mkdocs serve` and view at `localhost:8000/`.

## Testing

Run `./run-local.sh` from top level of the project.
Optionally specify a file path to run a specific test file e.g:
`./run-local.sh path/to/test/file/`

## Seeing the Coverage report

TODO
