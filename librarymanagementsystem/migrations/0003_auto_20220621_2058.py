# Generated by Django 3.0.5 on 2022-06-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanagementsystem', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=10),
        ),
    ]