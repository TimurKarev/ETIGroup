# Generated by Django 3.1.1 on 2020-10-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0002_auto_20201026_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='otkchecklist',
            name='Code_UE',
            field=models.CharField(default='жопа', max_length=10),
        ),
    ]
