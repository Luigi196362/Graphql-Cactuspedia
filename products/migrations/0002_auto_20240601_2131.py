# Generated by Django 3.1.3 on 2024-06-02 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='productDescription',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='productImage',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='productName',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='productPrice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='productStock',
        ),
    ]