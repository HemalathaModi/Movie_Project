from django.db import models
from django.contrib.auth.models import User

class Movieinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    image = models.ImageField(upload_to='movies/', blank = True, null = True)

    class Meta:
        db_table = 'movie_info'

    def __str__(self):
        return self.title

# Create your models here.
