# Generated by Django 2.0.5 on 2018-05-25 02:10

from django.db import migrations

def migrate(apps, schema_editor):
    Fanfic = apps.get_model('fanfics', 'Fanfic')
    Language = apps.get_model('fanfics', 'Language')

    for lang in Language.objects.all():
        correct_name = lang.name.strip()
        if lang.name != correct_name:
            lang.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('fanfics', '0008_fix_language_names'),
    ]

    operations = [
        migrations.RunPython(migrate)
    ]
