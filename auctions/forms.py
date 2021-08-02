from .models import Auction, Category
from django import forms


class AuctionCreateForm(forms.Form):
    categories = Category.objects.all().values_list('id', 'title')

    title = forms.CharField(max_length=255)
    description = forms.CharField( widget=forms.Textarea )
    starting_bid = forms.IntegerField()
    category = forms.ChoiceField(choices=categories)
    thumbnail = forms.ImageField()

    def save(self):
        data = self.cleaned_data

        category = Category.objects.get(pk=data['category'])

        auction = Auction(
            title = data['title'],
            description = data['description'],
            starting_bid = data['starting_bid'],
            category = category,
            thumbnail = data['thumbnail']
        )
        auction.save()