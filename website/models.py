from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    image = models.ImageField(upload_to="features/")

    def __str__(self):
        return self.title
    
class Pricing(models.Model):
    plan = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.plan
    

class Design(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="designs/")
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    