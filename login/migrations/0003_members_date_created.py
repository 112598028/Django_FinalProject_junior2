# Generated by Django 4.0 on 2022-04-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_members_email_alter_members_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
