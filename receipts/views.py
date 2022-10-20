from django.shortcuts import render, redirect
from receipts.models import ExpenseCategory, Receipt, Account
from django.contrib.auth.decorators import login_required
from .forms import ReceiptForm, ExpenseForm

# Create your views here.


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/create_receipt.html", context)


@login_required
def create_expensecategory(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.owner = request.user
            receipt.save()
            return redirect("category_list")
    else:
        form = ExpenseForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/create_category.html", context)


@login_required
def show_receipt(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_object": receipt,
    }
    return render(request, "receipts/receipts_list.html", context)


@login_required
def show_category(request):
    category = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories_object": category,
    }
    return render(request, "receipts/category_list.html", context)


@login_required
def show_account(request):
    account = Account.objects.filter(owner=request.user)
    context = {
        "accounts_object": account,
    }
    return render(request, "receipts/account_list.html", context)
