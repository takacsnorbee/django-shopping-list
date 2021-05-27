from django.db import models
from django.contrib.auth.models import User

class Shopping_list(models.Model):

    list_name = models.CharField(blank=False, max_length=60)
    list_items = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.list_name
