# Generated by Django 4.0 on 2022-04-14 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_flower_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]