# Generated by Django 3.1.3 on 2024-06-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postText',
            field=models.TextField(null=True),
        ),
    ]