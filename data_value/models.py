from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=220)
    money = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.money}"

class Country(models.Model):
    name = models.CharField(max_length=220)
    recovery = models.CharField(max_length=54)
    confirm = models.CharField(max_length=50)
    death = models.CharField(max_length=50)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} "

