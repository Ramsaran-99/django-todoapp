from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


STATUS = (
    ("Important", "Important"),
    ("Not Important", "Not Important"),
)

URGENCY = (
    ("Urgent", "Urgent"),
    ("Not Urgent", "Not Urgent"),
)

class List(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(choices=STATUS, max_length=50,blank=True,null=True)
    urgency=models.CharField(choices=URGENCY, max_length=50,blank=True,null=True)
    task_heading=models.TextField(blank=False,null=False)
    task=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    task_status=models.BooleanField(default=False)

    