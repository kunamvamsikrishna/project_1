from django.db import models

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)



class Phone(models.Model):
    name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    price=models.IntegerField()
    camera=models.CharField()
    battery=models.IntegerField()

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


