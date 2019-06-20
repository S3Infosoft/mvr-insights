# Generated by Django 2.2.2 on 2019-06-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/thumb/%Y/%m/'),
        ),
    ]