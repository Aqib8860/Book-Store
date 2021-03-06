# Generated by Django 3.2.10 on 2022-04-09 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('author', models.CharField(max_length=80)),
                ('price', models.CharField(max_length=12)),
                ('category', models.CharField(choices=[('Health', 'Health'), ('Games', 'Games'), ('Meetups', 'Meetups'), ('Music', 'Music'), ('Art', 'Art'), ('Food', 'Food'), ('Business', 'Business'), ('Sports', 'Sports')], max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_available', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
