from __future__ import unicode_literals

from django.db import models

class Courses(models.Model):
    course_name= models.CharField(max_length=255)
    description= models.TextField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
