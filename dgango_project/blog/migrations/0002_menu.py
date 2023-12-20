# Generated by Django 4.2.8 on 2023-12-19 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fImage', models.ImageField(upload_to='')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='blog.places')),
            ],
        ),
    ]
