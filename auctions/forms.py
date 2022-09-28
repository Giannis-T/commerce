from django.forms import ModelForm
from .models import Listing, Category, User

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"
        exclude = ('user',)

