from django.shortcuts import render
from receipts.models import ExpenseCategory, Receipt, Account
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def show_receipt(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_object": receipt,
    }
    return render(request, "receipts/receipts_list.html", context)
