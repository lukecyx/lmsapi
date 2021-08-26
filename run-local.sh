#!/usr/bin/env bash

#source venv/bin/activate
poetry shell

uwsgi \
	--socket /tmp/lms.sock \
	--module config.wsgi \
	--env=DJANGO_SETTINGS_MODULE=config.settings.local \
	--chmod-socket=666 \
	--processes=5 \
	--harakiri=20 \
	--vacuum \
	--py-auto-reload=2
