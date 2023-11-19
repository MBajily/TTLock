# Generated by Django 4.2.1 on 2023-11-19 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='lock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.lock'),
        ),
    ]
