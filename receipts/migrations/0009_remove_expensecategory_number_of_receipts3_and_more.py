# Generated by Django 4.1.2 on 2022-10-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "receipts",
            "0008_remove_expensecategory_number_of_receipts2_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expensecategory",
            name="number_of_receipts3",
        ),
        migrations.AddField(
            model_name="expensecategory",
            name="number_of_receipts",
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
