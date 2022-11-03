from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    user_id = models.IntegerField(blank=True, default=1)
    body = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    date_done = models.DateTimeField(blank=True)
