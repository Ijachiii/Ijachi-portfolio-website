# Generated by Django 4.1.1 on 2022-10-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email_address',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]