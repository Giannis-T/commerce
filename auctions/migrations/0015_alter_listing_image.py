# Generated by Django 4.1.1 on 2022-10-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0014_alter_listing_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.ImageField(
                upload_to="C:\\Users\\Giannis\\Desktop\\HarvardCS\\Projects\\commerce\\media"
            ),
        ),
    ]
