# Generated by Django 3.2.15 on 2022-09-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_course_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='photo_img',
            field=models.ImageField(blank=True, default='default', null=True, upload_to='photos'),
        ),
    ]