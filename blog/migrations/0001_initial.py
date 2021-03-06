# Generated by Django 3.2 on 2021-04-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
