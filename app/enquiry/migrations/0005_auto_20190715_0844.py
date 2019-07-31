# Generated by Django 2.2.3 on 2019-07-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0004_auto_20190624_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ota',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='contact_name',
        ),
        migrations.AddField(
            model_name='ota',
            name='contact_number',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partner',
            name='contact_number',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]