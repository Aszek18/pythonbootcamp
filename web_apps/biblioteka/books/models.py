from django.db import models

# Create your models here.
class Books (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    cover = models.ImageField(upload_to="books_covers/%Y/%m/&d")

    def __str__ (self):
        return f'{self.title} - {self.title}'
