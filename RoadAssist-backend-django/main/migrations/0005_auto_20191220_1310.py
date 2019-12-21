# Generated by Django 2.2.3 on 2019-12-20 13:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191220_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='rating',
            field=models.CharField(choices=[('1', 'Very Poor'), ('2', 'Below Average'), ('3', 'Average'), ('4', 'Minor issues'), ('5', 'Fine but can be improved')], max_length=1),
        ),
    ]