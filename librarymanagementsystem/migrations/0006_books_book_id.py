# Generated by Django 3.0.5 on 2022-06-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanagementsystem', '0005_auto_20220621_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_id',
            field=models.IntegerField(null=True),
        ),
    ]
