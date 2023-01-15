# Generated by Django 4.1.5 on 2023-01-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elite_eats_app', '0007_post_restaurant_alter_restaurant_name_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name_plural': 'Restaurants'},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='Elite_eats_app.tag'),
        ),
    ]