# Generated by Django 4.0.5 on 2022-06-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
