# Generated by Django 4.1.1 on 2022-10-03 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0016_alter_listing_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="C:\\Users\\Giannis\\Desktop\\HarvardCS\\Projects\\commerce\\media",
            ),
        ),
    ]
