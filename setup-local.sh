#!/usr/bin/env bash

[ "$EUID" -ne 0 ] && echo "Please run as root" && exit

python -m venv ./venv

source venv/bin/activate

pip install -r requirements-local.txt

CURRENTPATH=$(pwd)

sudo ln -s $CURRENTPATH/lms_nginx.conf /etc/nginx/sites-enabled/lms_nginx.conf

if (( ! $(grep -c "lms.local" /etc/hosts) )); then
	echo "127.0.0.1\tlms.local" >> /etc/hosts
else
	exit
fi
