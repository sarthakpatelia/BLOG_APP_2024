# Generated by Django 5.0.6 on 2024-05-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_follow_created_date_follow_muted'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(to='user_profile.follow'),
        ),
    ]