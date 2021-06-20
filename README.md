# LMSAPI v1

## Project Status

WIP (Work in Progress).

## Project Aim

An API that can be used to manage a standard book library, it's internal and its public facing needs.

## Ratioanle

This projects sole purpose is to learn about how to create an API without using Django Rest Framework.
It is to be used in conjunction with another fontend project, TBC.

## Technologies Being Used

* [Django v3.1][1]
* [django-rest-framework][2]

[1]: https://docs.djangoproject.com/en/3.1/
[2]: https://www.django-rest-framework.org/

## Setup and Running Locally

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

* As part of `./setup-local` the projects hostname (`lms.local/`) will be appended into your `/etc/hosts` file.
* `./setup-local` will also symlink `lms_nginx.conf` into `/etc/nginx/sites-enabled/` as `lms_nginx.conf`.

## Running Locally

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
