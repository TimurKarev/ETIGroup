# Generated by Django 3.1.1 on 2020-10-29 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0014_auto_20201029_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otkorder',
            name='tm_checklist',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='otk.tmchecklist'),
        ),
    ]
