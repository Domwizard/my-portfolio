#!/usr/bin/env bash
# exit on error
set -o errexit

# Устанавливаем зависимости
pip install -r requirements.txt

# Собираем статические файлы (CSS, JS)
python manage.py collectstatic --no-input

# Применяем миграции к базе данных
python manage.py migrate

# Создаем суперпользователя (админа)
# Команда || true нужна, чтобы сборка не упала, если админ уже создан
python manage.py createsuperuser --noinput --username admin --email admin@example.com || true
