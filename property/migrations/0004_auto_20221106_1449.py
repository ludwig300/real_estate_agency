from django.db import migrations, models


def compare_year(apps, schema_editor):
    apps.get_model('property', 'Flat').objects.update(
        new_building=models.F('construction_year') >= 2015
    )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(compare_year)
    ]
