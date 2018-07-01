from django.db import models


# модели создают колонки у меня в базе данных

class Alex(models.Model):
    content = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)