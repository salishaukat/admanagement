from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Category(models.Model):
    categoryName = models.CharField(max_length=500)

    def __str__(self):
        return self.categoryName


class Ad(models.Model):
    adText = models.CharField(max_length=500)
    adUrl = models.CharField(max_length=500)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    display_count = models.IntegerField(null=True, blank=True, default=0,db_index=True)
    createdby = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.adText

# Create your models here.
