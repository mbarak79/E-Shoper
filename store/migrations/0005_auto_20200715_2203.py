# Generated by Django 3.0.8 on 2020-07-15 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200715_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='CATDesc',
        ),
        migrations.RemoveField(
            model_name='category',
            name='CATImg',
        ),
    ]
