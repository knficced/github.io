from django.db import models


class Article(models.Model):
    title = models.CharField('ФИО', max_length=50)
    Stat = models.CharField('Электронная почта', max_length=100)
    full_text = models.TextField('Текст сообщения', max_length=300)
    date = models.DateField('Дата написания')

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
