#!/bin/bash


sleep 10
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
