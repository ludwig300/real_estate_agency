# Generated by Django 2.2.24 on 2022-11-18 11:45

from django.db import migrations


def copy_fields(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_deprecated = flat.owner
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_flat_owner_deprecated'),
    ]

    operations = [
        migrations.RunPython(copy_fields),
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        )
    ]
