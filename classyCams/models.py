from django.db import  models


class country(models.Model):
    name        = models.CharField(max_length=45)
    # tld         = models.CharField(max_length=28)
    code        = models.CharField(max_length=3)
