from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class StockEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    time = models.DateField(auto_now_add=True)
