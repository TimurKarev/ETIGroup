# Generated by Django 3.1.1 on 2020-11-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otk', '0051_auto_20201123_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourchoisepoint',
            name='choice',
            field=models.CharField(choices=[('Не проверено', 'Unchecked'), ('Не используется', 'Unused'), ('Принято', 'Appoved'), ('Коментарий', 'Comment')], default='Не проверено', max_length=15),
        ),
    ]
