# Generated by Django 2.2.3 on 2019-12-20 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20191220_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='places',
            options={'verbose_name_plural': 'Places'},
        ),
        migrations.AlterModelOptions(
            name='roads',
            options={'verbose_name_plural': 'Roads'},
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Just Arrived'), ('1', 'In Progress'), ('2', 'Resolved')], max_length=1)),
                ('rating', models.IntegerField(default=5)),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Roads')),
            ],
            options={
                'verbose_name_plural': 'Complaints',
            },
        ),
    ]
