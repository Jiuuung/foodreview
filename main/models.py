from django.db import models
from config.settings import AUTH_USER_MODEL



# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    introduce = models.TextField()
    opentime=models.TimeField(blank=True, null=True)
    closetime=models.TimeField(blank=True, null=True)
    recommend = models.ManyToManyField(AUTH_USER_MODEL)
    score =models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    food=models.CharField(max_length=10)
    price=models.IntegerField(default=0)

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reviewer=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    star=models.IntegerField(default=0)
    create_date= models.DateTimeField()