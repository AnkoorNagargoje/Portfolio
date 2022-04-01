# Generated by Django 4.0.3 on 2022-04-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Startups', 'Startups'), ('Web Development', 'Web Development'), ('My Journey', 'My Journey'), ('Django', 'Django'), ('Social Media', 'Social Media')], default='My Journey', max_length=100)),
                ('read_time', models.PositiveIntegerField(default=0)),
                ('image_url', models.CharField(max_length=100)),
            ],
        ),
    ]