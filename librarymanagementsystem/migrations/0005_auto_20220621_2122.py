# Generated by Django 3.0.5 on 2022-06-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanagementsystem', '0004_auto_20220621_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.CharField(max_length=50),
        ),
    ]
