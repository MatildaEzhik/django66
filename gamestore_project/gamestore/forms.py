from django import forms
from gamestore.models import Game
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'genre', 'price', 'release_date', 'platforms', 'image']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("цена не может быть отрицательной")
        return price
