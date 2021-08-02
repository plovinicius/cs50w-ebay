from django.contrib import admin
from .models import Comment, Category, Auction, Bid

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'auction', 'comment', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'starting_bid', 'created_at')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'auction', 'created_at')