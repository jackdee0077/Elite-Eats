# Generated by Django 4.1.5 on 2023-01-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elite_eats_app', '0002_auto_20230105_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisine',
        ),
    ]