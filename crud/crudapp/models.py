from django.db import models

# Create your models here.

class Blog(models.Model):
    objects = models.Manager()
    title=models.CharField(null = True, max_length=100)
    writer= models.CharField(null = True, max_length=200)
    pub_date = models.DateField()
    body= models.TextField(null = True)
    applicant = models.IntegerField(default=0)

def __str__(self):
    return self.title