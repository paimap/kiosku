from django.forms import ModelForm
from main.models import StockEntry

class StockEntryForm(ModelForm):
    class Meta:
        model = StockEntry
        fields = ["name", "description", "price", "quantity"]