# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Item, ItemSizes


class ItemSizesForm(forms.ModelForm):
    sizes = forms.CharField(label="Sizes (comma-separated)", max_length=100)
    stocks = forms.CharField(label="Stocks (comma-separated)", max_length=100)

    class Meta:
        model = ItemSizes
        fields = ["item"]

    def save(self, commit=True):
        item_sizes = super().save(commit=False)

        sizes = self.cleaned_data["sizes"].split(",")
        stocks = self.cleaned_data["stocks"].split(",")

        # Ensure that the number of sizes and stocks match
        if len(sizes) != len(stocks):
            raise ValueError("Number of sizes and stocks do not match.")

        # Save the item sizes
        for size, stock in zip(sizes, stocks):
            stock = int(stock.strip())
            if stock <= 0:
                raise ValidationError("Stock must be a positive integer.")
            else:
                item_sizes = ItemSizes.objects.create(
                    item=item_sizes.item, size=size.strip(), stock=stock
                )
                return item_sizes


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            "name",
            "type",
            "attributes",
            "thumbnail",
            "original_price",
            "retail_price",
            "manufacturing_cost",
        ]
