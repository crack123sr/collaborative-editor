# Generated by Django 5.1.1 on 2024-09-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_alter_room_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='0D4CF3', max_length=10, unique=True),
        ),
    ]