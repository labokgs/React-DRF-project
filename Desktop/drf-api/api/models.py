from django.db import models

# Create your models here.
#　データベースの構造を定義するのがmodels.py

class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title