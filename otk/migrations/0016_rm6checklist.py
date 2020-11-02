# Generated by Django 3.1.1 on 2020-11-02 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0015_auto_20201029_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='RM6CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(blank=True, default='', max_length=20, verbose_name='Заводской номер')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otk.tmchecklist')),
            ],
        ),
    ]
