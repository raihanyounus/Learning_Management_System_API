# Generated by Django 3.2 on 2021-06-02 03:12

import coupon.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0005_auto_20210526_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('discount', models.IntegerField()),
                ('code', models.CharField(default=coupon.models.random_code, max_length=6, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='course.course')),
            ],
        ),
    ]
