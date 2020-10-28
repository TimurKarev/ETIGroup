# Generated by Django 3.1.1 on 2020-10-28 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0009_auto_20201028_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otkorder',
            name='tm_checklist',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='otk.tmchecklist'),
        ),
        migrations.AlterField(
            model_name='tmchecklist',
            name='UE_Code',
            field=models.CharField(default=None, max_length=20, verbose_name='Шифр(УЭ)'),
        ),
    ]
