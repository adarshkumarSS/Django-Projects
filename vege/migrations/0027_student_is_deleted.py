# Generated by Django 5.0.7 on 2024-07-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0026_receipes_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
