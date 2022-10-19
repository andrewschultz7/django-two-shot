from django.shortcuts import render
from .models import ExpenseCategory, Receipt, Account

# Create your views here.


def show_receipt(request):
    receipt = Receipt.objects.all()
    context = {
        "receipts": receipt,
    }
    return render(request, "receipts/receipts.html", context)
