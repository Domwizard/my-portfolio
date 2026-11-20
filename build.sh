#!/usr/bin/env bash
# exit on error
set -o errexit

# Устанавливаем зависимости
pip install -r requirements.txt

# Собираем статические файлы (CSS, JS)
python manage.py collectstatic --no-input

# Применяем миграции к базе данных
python manage.py migrate
