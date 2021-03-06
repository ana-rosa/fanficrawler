# Generated by Django 2.0.5 on 2018-05-25 01:28

import time
from django.db import migrations

def migrate(apps, schema_editor):
    Fanfic = apps.get_model('fanfics', 'Fanfic')
    Language = apps.get_model('fanfics', 'Language')
    languages = {}

    t0 = time.time()
    count = 0
    for fanfic in Fanfic.objects.all():
        if fanfic.language not in languages:
            language, _ = Language.objects.get_or_create(name=fanfic.language)
            languages[fanfic.language] = language
        else:
            language = languages[fanfic.language]

        count += 1
        if count % 100 == 0:
            print('count={}, time={}'.format(count, time.time() - t0))

        fanfic.lang = language
        fanfic.save()


class Migration(migrations.Migration):

    dependencies = [
        ('fanfics', '0003_auto_20180525_0127'),
    ]

    operations = [
        migrations.RunPython(migrate)
    ]
