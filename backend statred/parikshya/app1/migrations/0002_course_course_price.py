# Generated by Django 3.2.15 on 2022-09-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Course_price',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
