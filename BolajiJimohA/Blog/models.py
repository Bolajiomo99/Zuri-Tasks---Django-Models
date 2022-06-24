from collections import UserDict
from typing import get_args
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text =  models.TextField(default= 500)
    author = models.get_user_model
    created_date = models.DateTimeField
    published_date = models.DateTimeField

    def _str_(self) -> str:
        return self.title

    



