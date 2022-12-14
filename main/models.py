from django.db import models
from config.settings import AUTH_USER_MODEL



# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    introduce = models.TextField()
    opentime=models.TimeField(blank=True, null=True)
    closetime=models.TimeField(blank=True, null=True)
    recommend = models.ManyToManyField(AUTH_USER_MODEL, blank=True)
    score =models.FloatField(default=0)

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    food=models.CharField(max_length=10)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.food

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    reviewer=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    star=models.FloatField(default=2.5)
    create_date= models.DateTimeField()
    def __str__(self):
        return self.reviewer