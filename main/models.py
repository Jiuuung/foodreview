from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    introduce = models.TextField()
    #recommend = models.ManyToManyField

    def __str__(self):
        return self.title

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    content = models.TextField()
    create_date= models.DateTimeField()