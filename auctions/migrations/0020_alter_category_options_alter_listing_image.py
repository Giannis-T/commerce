# Generated by Django 4.1.1 on 2022-10-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0019_alter_listing_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category", options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.ImageField(
                default="C:\\Users\\Giannis\\Desktop\\HarvardCS\\Projects\\media\\default-placeholder-image.jpg",
                upload_to="C:\\Users\\Giannis\\Desktop\\HarvardCS\\Projects\\media",
            ),
        ),
    ]
