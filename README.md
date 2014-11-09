phone_directory
==============

Assigns phones numbers to new users

## Dependencies

Some Common System dependencies are the following

Python 2.7.3 (available via apt in debian "wheezy") or 2.7.5+ (in ubuntu 13.10)
wget 1.13+ (older versions could not connect to PyPi via HTTPS)
pip 1.1 (available via apt in debian wheezy as python-pip)
git
libbz2-dev
libffi-dev
libicu-dev
libjpeg-dev
libpython-dev

## Install

* Get the repository from github.
	1. `git@github.com:AdrielVelazquez/phone_direcoty.git`

* Create the local DB and virtualenv
    1. `make install`

## Run Server

. ./bin/activate && python server.py

## Configurations

Configs can be altered with

`export PHONE_NUMBER_CONFIG= <server_home_dir>/location/of/config-prod.py`

## Tests

`make test`

## Endpoints

/SET/number

Arguments:
    user, required, "Assigned number gets placed a user"
    number, not required, "Select a custom number"


/SET/unassign

Arguments:
    number, required, "Unassign a number from it's user"


/SET/assigned

Arguments:
    user, required, "Get list of numbers assigned to user"
