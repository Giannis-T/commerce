# Generated by Django 4.1.1 on 2022-09-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0010_auto_20210729_1131"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing", name="image", field=models.ImageField(upload_to=""),
        ),
    ]
