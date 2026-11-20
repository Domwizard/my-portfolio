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
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='vladimir').exists() or User.objects.create_superuser('vladimir', 'admin@example.com', os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Vladimir2026Super!'))"
