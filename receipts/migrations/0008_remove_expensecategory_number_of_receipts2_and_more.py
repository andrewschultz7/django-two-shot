# Generated by Django 4.1.2 on 2022-10-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "receipts",
            "0007_rename_number_of_receipts_expensecategory_number_of_receipts2_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expensecategory",
            name="number_of_receipts2",
        ),
        migrations.AddField(
            model_name="expensecategory",
            name="number_of_receipts3",
            field=models.CharField(max_length=50, null=True),
        ),
    ]