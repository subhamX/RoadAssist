# Generated by Django 2.2.3 on 2019-12-20 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='roads',
            name='end',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_of_road_ending', to='main.Places'),
        ),
        migrations.AlterField(
            model_name='roads',
            name='start',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Places'),
        ),
    ]
