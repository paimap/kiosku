from django.db import models

# Create your models here.
from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    npm = models.TextField()
    nama = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
