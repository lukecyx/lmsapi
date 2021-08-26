#!/usr/bin/env bash

# Run all unit tests. These are files that start with test_* in each 'app'.
# Optionally pass a path as the first arg to the script to run a specific file

#source ./venv/bin/activate

#user="$(whoami)"
#run_local_pid="$(pgrep -u $user -f run-local.sh | awk '{print $1}')"

# If already running locally, just run pytest for the full test suite. Otherwise,
# run the server and then pytest.
#[ $run_local_pid ] && pytest $@ || bash ./run-local.sh &>/dev/null & pytest $@

# So now using poetry all I have to do this is...
poetry run pytest
