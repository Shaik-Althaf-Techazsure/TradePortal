set -e

python wait_for_db.py

echo "MySQL database is ready. Running migrations..."
python manage.py migrate

echo "Migrations complete. Starting server..."

exec python manage.py runserver 0.0.0.0:8000