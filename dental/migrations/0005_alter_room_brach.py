# Generated by Django 5.0 on 2024-01-09 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dental', '0004_remove_dentalbraches_user_dentalbraches_doctor_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='brach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_room', to='dental.dentalbraches'),
        ),
    ]