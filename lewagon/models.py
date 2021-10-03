from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Update(models.Model):
  text = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.PROTECT)

  def __str__(self):
    return f"{self.text} - {self.user}"