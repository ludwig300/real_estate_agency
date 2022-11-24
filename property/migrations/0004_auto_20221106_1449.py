from django.db import migrations


def compare_year(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for building in Flat.objects.all().iterator():
        building.new_building = building.construction_year >= 2015
        building.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(compare_year)
    ]
