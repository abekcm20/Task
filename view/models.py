from django.db import models

# Create your models here.


# Create your models here.

class display(models.Model):
    sid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    ParentID = models.IntegerField(default=None,blank=True, null=True)

    def __str__(self):
        return f"{self.sid} , {self.title} , {self.ParentID}"