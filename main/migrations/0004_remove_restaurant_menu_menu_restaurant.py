# Generated by Django 4.1.3 on 2022-11-30 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_menu_restaurant_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.restaurant'),
        ),
    ]
