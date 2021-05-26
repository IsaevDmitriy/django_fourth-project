from django.db import models



class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.NullBooleanField()
    slug = models.SlugField()

