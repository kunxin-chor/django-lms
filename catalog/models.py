from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    number_of_hours = models.IntegerField(blank=False)
    instructor = models.ForeignKey('Instructor', blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title
    
class Instructor(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name