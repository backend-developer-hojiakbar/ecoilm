# Generated by Django 4.2.1 on 2023-10-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xamkorlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='xamkorImg/')),
            ],
        ),
    ]
