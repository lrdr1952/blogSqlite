# Generated by Django 4.1.3 on 2022-12-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='Profiles'),
        ),
    ]
