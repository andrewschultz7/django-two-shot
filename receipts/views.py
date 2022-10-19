from django.shortcuts import render
from receipts.models import ExpenseCategory, Receipt, Account

# Create your views here.


def show_receipt(request):
    receipt = Receipt.objects.all()
    context = {
        "receipts_object": receipt,
    }
    return render(request, "receipts/receipts_list.html", context)
