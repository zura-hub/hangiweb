# Generated by Django 5.0.2 on 2024-03-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_team', '0004_groupphoto_description_alter_groupphoto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupphoto',
            name='image',
            field=models.ImageField(upload_to='groupphotopy_photos/'),
        ),
    ]