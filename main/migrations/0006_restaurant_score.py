# Generated by Django 4.1.3 on 2022-11-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_review_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]