from typing import Iterable, Optional
from django.db import models

# Create your models here.

class student(models.Model):
    class Meta:
        db_table = 'student'
        verbose_name_plural = 'students'
        managed = True
        ordering = ['-id']

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='student_images/', default='', null=True)
    section = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    # def save(self, str=None, args=None):
    #     return super().save()
