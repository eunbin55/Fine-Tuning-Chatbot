from django.db import models

# Create your models here.

class BoardPost (models.Model):
    title= models.CharField(max_length=200)
    content=models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     def __str__(self) :
#         return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.title