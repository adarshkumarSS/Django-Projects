# Generated by Django 5.0.7 on 2024-07-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0011_alter_receipes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipes',
            name='recipi_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
