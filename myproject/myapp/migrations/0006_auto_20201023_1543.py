# Generated by Django 2.2 on 2020-10-23 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201023_1409'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategories',
            new_name='ProductCategory',
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={},
        ),
    ]
