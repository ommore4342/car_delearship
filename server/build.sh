#!/usr/bin/env bash
# Render build script — runs inside the server/ directory

set -e

echo "==> Installing Python dependencies"
pip install -r requirements.txt

echo "==> Running migrations"
python manage.py migrate --noinput

echo "==> Seeding dealer & review data"
python manage.py seed_data

echo "==> Collecting static files"
python manage.py collectstatic --noinput
