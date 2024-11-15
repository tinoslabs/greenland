# Generated by Django 5.1.3 on 2024-11-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenlandapp', '0004_products_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShadeCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(blank=True, max_length=100, null=True)),
                ('card_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
