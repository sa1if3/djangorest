from django.db import models

# Create your models here.

class Quote(models.Model):
    author = models.CharField(max_length=50)
    quote = models.CharField(max_length=200)
    def __str__(self):
        return self.author