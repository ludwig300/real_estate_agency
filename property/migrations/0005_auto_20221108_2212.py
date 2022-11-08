# Generated by Django 2.2.24 on 2022-11-08 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20221106_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(null=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Flat', verbose_name='Квартира, на которую пожаловались')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]
