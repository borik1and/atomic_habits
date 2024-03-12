# Generated by Django 4.2.7 on 2024-03-12 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0011_remove_habit_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.DurationField(default=datetime.timedelta(days=1), verbose_name='Периодичность выполнения'),
        ),
    ]
