#!/usr/bin/env bash
# Render build script - runs on every deploy
# Fails fast if any command errors (no partial/broken deploys)
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Gather static files into STATIC_ROOT so whitenoise can serve them
python manage.py collectstatic --no-input

# Apply any pending database migrations
python manage.py migrate
