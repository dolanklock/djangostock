from django import forms
from . import models


class StockForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ["ticker"]
