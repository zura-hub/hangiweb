# Generated by Django 5.0.2 on 2024-02-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='phartner')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('title_ka', models.CharField(max_length=200, null=True)),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
                ('content_ka', models.TextField(null=True)),
            ],
        ),
    ]
