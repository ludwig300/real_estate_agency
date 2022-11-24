# Generated by Django 2.2.24 on 2022-11-12 15:39

from django.db import migrations


def copy_fields(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221117_2112'),
    ]

    operations = [
        migrations.RunPython(copy_fields)
    ]
