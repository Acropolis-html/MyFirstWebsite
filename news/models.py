from django.db import models
from django.contrib.auth.models import User
# CharField нужен для маленьких текстов типо названия
# А TextField соответственно нужен для текстов

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='articles')
    date = models.DateTimeField('Время')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
