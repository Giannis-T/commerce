from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.title}"


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=128)
    cost = models.FloatField(default=0)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    time_created = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.title}"


class Watchlist(models.Model):
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    cost = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.IntegerField()
    




