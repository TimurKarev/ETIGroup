# Generated by Django 3.1.1 on 2020-11-24 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0052_auto_20201124_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourchoisepoint',
            name='choice',
            field=models.CharField(choices=[('Не проверено', 'Не проверено'), ('Не используется', 'Не используется'), ('Принято', 'Принято'), ('Коментарий', 'Коментарий')], default='Не проверено', max_length=15),
        ),
        migrations.CreateModel(
            name='SubstationTypePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('choice', models.CharField(choices=[('БКТП', 'БКТП')], default='БКТП', max_length=15)),
                ('checklist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='otk.chlistsection')),
            ],
            options={
                'db_table': 'substationpoint',
            },
        ),
        migrations.CreateModel(
            name='IntegerPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('integer', models.IntegerField(blank=True, default=0)),
                ('checklist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='otk.chlistsection')),
            ],
            options={
                'db_table': 'integerpoint',
            },
        ),
    ]
