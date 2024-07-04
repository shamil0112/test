from django.db import models

# Create your models here.


class BooksForm(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    
    def __str__(self):
        return self.title