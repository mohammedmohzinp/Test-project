# Generated by Django 3.2 on 2021-04-21 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
