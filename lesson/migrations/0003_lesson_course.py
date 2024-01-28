# Generated by Django 4.2.7 on 2024-01-27 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_preview'),
        ('lesson', '0002_alter_lesson_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course.course', verbose_name='курс'),
            preserve_default=False,
        ),
    ]