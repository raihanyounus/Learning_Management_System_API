# Generated by Django 3.2 on 2021-06-07 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import review.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0006_course_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=300)),
                ('rating', models.IntegerField(validators=[review.models.rating_validation])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
