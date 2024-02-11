# Generated by Django 4.2.7 on 2024-02-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderators')], default='member', max_length=9, verbose_name='Роль'),
        ),
    ]