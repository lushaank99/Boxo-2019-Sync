from django.db import models

# Create your models here.

class Books(models.Model):
    book = models.CharField(max_length=150,null=True,blank=True)
    genre = models.CharField(max_length=150,null=True)
    published = models.CharField(max_length=150,null=True)
    poster = models.URLField(max_length=200, null=True)
    author = models.CharField(max_length=150,null=True)


    def __str__(self):
        return self.book+' /// '+self.genre+' /// '+self.published+' /// '+self.poster+' /// '+self.author




