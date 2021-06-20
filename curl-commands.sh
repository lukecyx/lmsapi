#!/usr/bin/env bash

# set -x  # echo on

#echo -e "\e[1mtest endopoint\e[0m"
#echo "URL = /users/test/"
#curl -H "Accept: application/json" \
#	-H "Content-Type: application/json" \
#	-H "X-CSRFToken: XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4" \
#	-b 'csrftoken=XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4' \
#	-X POST \
#	http://lms.local/users/test/

#echo 
### MISC CRAP used to figure out correct way I needed to send CSRF token to Django. ###
# -H "X-CSRFToken: XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4" \#
# -b 'X-CSRFToken=XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4' \
# -b 'csrftoken=XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4' \
# -b 'csrftoken=XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4' \

#echo -e "\e[1mUser Create Post Request\e[0m"
 curl -H "Accept: application/json" \
	 -H "Content-Type: application/json" \
	 -H "X-CSRFToken: XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4" \
	 -b 'csrftoken=XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4' \
	 -X POST \
	 -d '{"data": "bar"}' \
	 http://lms.local/users/create/
#curl -H "Accept: application/json" \
#	-H "Content-Type: application/json" \
#	-H "X-CSRFToken: XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4" \
#	-b 'csrftoken=XH4XwRUFtW982vLQfJzmcMT5QZtKTEa5DF7KYuREAqsCEn5F17iRe5KZZAUdNAR4' \
#	-X POST \
#	-d '{"data": "bar"}'
 # 	http://lms.local/dummy/
#echo
#echo
#curl -H "Accept: application/json" \
# -H "Content-Type: application/json" \
# http://lms.local/dummy/

#curl -H "Accept: application/json" \
#  -H "Content-Type: application/json" \
#  http://lms.local/dummy
