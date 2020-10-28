# Generated by Django 3.1.1 on 2020-10-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0007_auto_20201027_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tm_checklist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='otk.tmchecklist')),
            ],
        ),
    ]
