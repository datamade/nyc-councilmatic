#!/bin/bash

set -e

python manage.py migrate
python manage.py createcachetable
python manage.py import_data
