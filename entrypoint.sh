#!/bin/sh
set -e

echo ">>> Attente de MySQL..."
until python -c "
import MySQLdb
MySQLdb.connect(
    host='$DB_HOST',
    user='$DB_USER',
    passwd='$DB_PASSWORD',
    db='$DB_NAME'
)" 2>/dev/null; do
  sleep 2
done
echo ">>> MySQL prêt."

echo ">>> Migrations..."
python manage.py migrate --noinput

echo ">>> Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo ">>> Démarrage Gunicorn..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
