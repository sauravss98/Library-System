# Generated by Django 4.2.5 on 2024-01-31 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authorName',
            new_name='author_name',
        ),
    ]
