# Generated by Django 4.2.1 on 2023-08-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_ttlock_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
