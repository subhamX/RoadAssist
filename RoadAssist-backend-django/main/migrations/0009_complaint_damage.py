# Generated by Django 2.2.3 on 2019-12-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191220_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='damage',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]