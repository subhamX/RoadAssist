# Generated by Django 2.2.3 on 2019-12-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_complaint_status_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images'),
        ),
    ]
