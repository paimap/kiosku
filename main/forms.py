from django.forms import ModelForm
from main.models import StockEntry
from django.utils.html import strip_tags

class StockEntryForm(ModelForm):
    class Meta:
        model = StockEntry
        fields = ["name", "description", "price", "quantity"]

    def clean_mood(self):
        mood = self.cleaned_data["mood"]
        return strip_tags(mood)

    def clean_feelings(self):
        feelings = self.cleaned_data["feelings"]
        return strip_tags(feelings)