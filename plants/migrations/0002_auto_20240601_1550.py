# Generated by Django 3.1.3 on 2024-06-01 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='type',
            new_name='type_plant',
        ),
    ]