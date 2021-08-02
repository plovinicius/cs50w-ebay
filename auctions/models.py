from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Auction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    starting_bid = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='auctions')
    thumbnail = models.ImageField(upload_to='thumbnails')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name='bids')
    auction = models.ForeignKey(Auction, models.CASCADE, related_name='bids')
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bid {self.value} on {self.auction.title}"


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
