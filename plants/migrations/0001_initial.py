# Generated by Django 3.1.3 on 2024-06-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantName', models.TextField()),
                ('plantType', models.TextField()),
                ('plantOrigin', models.TextField()),
                ('plantDescription', models.TextField()),
                ('plantImage', models.TextField()),
            ],
        ),
    ]
