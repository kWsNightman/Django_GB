# Generated by Django 3.2.5 on 2021-07-11 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'корзина', 'verbose_name_plural': 'корзины'},
        ),
        migrations.AddField(
            model_name='basket',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]