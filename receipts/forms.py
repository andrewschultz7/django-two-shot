from django.forms import ModelForm
from .models import Receipt, ExpenseCategory


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]


class ExpenseForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            "name",
        ]
