#!/usr/bin/env bash


export FLASK_ENV=development

FLASK_APP=test.py flask run &

sleep 2

curl -i http://localhost:5000/

kill %1

echo
echo
