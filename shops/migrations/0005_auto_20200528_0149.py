# Generated by Django 2.0.5 on 2020-05-27 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_auto_20200528_0137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
