# Generated by Django 4.1.3 on 2022-12-02 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_alter_menu_restaurant_alter_restaurant_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.restaurant'),
        ),
        migrations.AlterField(
            model_name='review',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.menu'),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.restaurant'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
