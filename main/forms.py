from django.forms import ModelForm
from main.models import MarketStock

class ProductForm(ModelForm):
    class Meta:
        model = MarketStock
        fields = ["name", "price", "description", "amount", "category"]