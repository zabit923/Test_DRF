from django.contrib.auth.models import User
from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.TextField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
