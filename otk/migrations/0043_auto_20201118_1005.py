# Generated by Django 3.1.1 on 2020-11-18 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0042_auto_20201118_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chlistsection',
            name='checklist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='otk.checklist'),
        ),
    ]