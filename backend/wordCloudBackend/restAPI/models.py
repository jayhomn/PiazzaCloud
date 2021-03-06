from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class CourseName(models.Model):
    courseName = models.CharField(max_length=100)

class UserProfile(models.Model):
    userName = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    successLogin = models.BooleanField(default=False)
    listCourses = models.ManyToManyField(CourseName)


# class Course(models.Model):
#     courseName = models.CharField(max_length=100)