# Generated by Django 3.2 on 2021-05-28 03:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0003_textchapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('video_id', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=10000)),
                ('video_plateform', models.CharField(choices=[('Y', 'Youtube'), ('V', 'Vimeo')], max_length=2)),
                ('lecture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='video_chapter', to='chapter.chapter')),
            ],
        ),
    ]
