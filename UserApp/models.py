from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20 , unique=True )
    join_date = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    password =models.CharField(max_length=500, null=False)

    def __str__(self):
        return f"{self.uid} , {self.username} , {self.join_date}, {self.password}"



class tasks(models.Model):
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User , on_delete=models.PROTECT , related_name="user")
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=2000, default=None, blank=True, null=True)
    task_pic = models.ImageField(upload_to='static' ,default=None, blank=True, null=True)
    timestamp = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.tid} , {self.task_title} , {self.task_description}"