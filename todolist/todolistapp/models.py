from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoListModel(models.Model):
    text = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f'Item: {self.text} | Owner: {self.user.first_name} | '