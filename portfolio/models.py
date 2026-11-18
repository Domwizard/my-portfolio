from django.db import models

class Profile(models.Model):
    name = models.CharField('Имя', max_length=150)
    headline = models.CharField('Заголовок', max_length=200, help_text='Python разработчик')
    bio = models.TextField('О себе')
    image = models.ImageField("Картинка", upload_to="projects/", blank=True, null=True)
    email = models.EmailField('Email', blank=True)
    tg = models.CharField('Telegram', max_length=100, blank=True)
    gb = models.URLField('GitHub', blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    def __str__(self):
        return self.name

class Sckill(models.Model):
    name = models.CharField('Название', max_length=100)
    order = models.PositiveSmallIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    photo = models.ImageField('Картинка', upload_to='projects/', blank=True, null=True)
    url = models.URLField('Ссылка на проект', blank=True)
    tech = models.CharField('Технологии', max_length=200, help_text='Через запятую: Django, PostgreSQL, Bootstrap')
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    is_published = models.BooleanField("Опубликован", default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title