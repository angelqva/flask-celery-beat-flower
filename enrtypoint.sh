#!/bin/sh
cd /app
flask db init
flask db migrate
flask db upgrade
exec "$@"