# Generated by Django 4.2.8 on 2023-12-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_person_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=20)),
                ('pImage', models.ImageField(upload_to='')),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=20)),
                ('pImage', models.ImageField(upload_to='')),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
