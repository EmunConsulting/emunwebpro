# Generated by Django 5.0.7 on 2024-08-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelers', '0002_alter_profileimage_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='profile_image',
            field=models.ImageField(upload_to='profile_image/'),
        ),
    ]
