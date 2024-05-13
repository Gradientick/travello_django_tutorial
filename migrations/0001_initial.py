# Generated by Django 5.0.6 on 2024-05-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]