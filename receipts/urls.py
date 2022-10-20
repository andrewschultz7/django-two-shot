from django.urls import path
from .views import (
    show_receipt,
    create_receipt,
    create_expensecategory,
    show_category,
    show_account,
)

urlpatterns = [
    path("", show_receipt, name="home"),
    path("categories/create/", create_expensecategory, name="create_category"),
    path("accounts/", show_account, name="account_list"),
    path("categories/", show_category, name="category_list"),
    path("create/", create_receipt, name="create_receipt"),
]
