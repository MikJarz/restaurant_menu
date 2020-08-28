# Generated by Django 3.1 on 2020-08-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='food',
            field=models.ManyToManyField(to='menu.FoodItem'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]