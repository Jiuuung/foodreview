# Generated by Django 4.1.3 on 2022-11-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_restaurant_menu_menu_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.IntegerField(default=0),
        ),
    ]
