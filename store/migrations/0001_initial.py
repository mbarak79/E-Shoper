# Generated by Django 3.0.8 on 2020-07-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sportswear', models.CharField(max_length=50)),
                ('men', models.CharField(max_length=50)),
                ('women', models.CharField(max_length=50)),
                ('kids', models.CharField(max_length=50)),
                ('bags', models.CharField(max_length=50)),
                ('shoes', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]