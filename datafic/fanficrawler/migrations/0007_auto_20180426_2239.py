# Generated by Django 2.0.4 on 2018-04-27 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanficrawler', '0006_auto_20180426_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanfic',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fanfic',
            name='words',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
