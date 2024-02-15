# Generated by Django 4.2.7 on 2024-02-15 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_owner'),
        ('users', '0006_alter_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed', models.BooleanField(default=False, verbose_name='подписался')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='course.course', verbose_name='курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'unique_together': {('user', 'course')},
            },
        ),
    ]