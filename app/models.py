from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=150)
    active = models.BooleanField()
    def __str__(self):
        return self.category_name

class Branche(models.Model):
    branch_name = models.CharField(max_length = 150)
    def __str__(self):
        return self.branch_name

class Student(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='media/', max_length=100,null=True)
    roll_no = models.CharField(max_length = 150)
    branch = models.ForeignKey('Branche', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True)
    roll_no = models.CharField(max_length=150,null=True)
    score = models.CharField(max_length=150,null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branche', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
