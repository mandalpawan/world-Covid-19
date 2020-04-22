from django.db import models

# Create your models here.
class Feedback(models.Model):
    name =    models.CharField(max_length=40)
    email =   models.EmailField(max_length=50)
    message = models.TextField()
    date =    models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class update_log(models.Model):
    feature = models.BooleanField()
    improvement = models.BooleanField()
    fix = models.BooleanField()
    subheader = models.CharField(max_length=40)
    content = models.TextField()
    update_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subheader


class Crona_data(models.Model):
    country =    models.CharField(max_length=40)
    total_case =    models.CharField(max_length=40)
    new_cases =    models.CharField(max_length=40)
    total_death =    models.CharField(max_length=40)
    new_death =    models.CharField(max_length=40)
    total_recovery =    models.CharField(max_length=40)
    active_cases =    models.CharField(max_length=40)
    serious_critical =    models.CharField(max_length=40)
    total_case_perM =    models.CharField(max_length=40)
    totalDeathperM =    models.CharField(max_length=40)
    total_test_perM =    models.CharField(max_length=40)
    test_perM =    models.CharField(max_length=40)
    continent =    models.CharField(max_length=40)
    update_date =  models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.country


