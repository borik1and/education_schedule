# Generated by Django 4.2.7 on 2024-02-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_payment_payment_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата последнего входа'),
        ),
    ]