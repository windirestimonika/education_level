from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    majors = models.CharField(max_length=100)
    entry_date = models.DateField(max_length=100)
    graduate_date = models.DateField(max_length=100)
    scholarship = models.BooleanField(default=False)
    grade = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    