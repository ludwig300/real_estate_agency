from django.db import migrations


def compare_year(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for building in Flat.objects.all():
        if building.construction_year >= 2015:
            flag = True
        else:
            flag = False

        building.new_building = flag
        building.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(compare_year)
    ]
