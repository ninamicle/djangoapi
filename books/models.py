from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, null=True)
    language = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.title
