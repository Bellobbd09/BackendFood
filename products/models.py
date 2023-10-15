from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class food(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='food')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    active = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)



