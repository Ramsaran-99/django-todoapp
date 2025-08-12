from django.db import models

# Create your models here.

class List(models.Model):
    task_heading=models.TextField(blank=False,null=False)
    task=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    task_status=models.BooleanField(default=False)

    