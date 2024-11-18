#!/bin/sh
poetry install
poetry run flaks db upgrade
poetry run python ./app/app.py
