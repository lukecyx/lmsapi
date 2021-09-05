!#/usr/bin/env bash

set -e

echo "Performing initial setup..."

docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
docker-compose logs -f
