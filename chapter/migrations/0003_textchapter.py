# Generated by Django 3.2 on 2021-05-28 01:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0002_linkchapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=10000)),
                ('lecture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='text_chapter', to='chapter.chapter')),
            ],
        ),
    ]
