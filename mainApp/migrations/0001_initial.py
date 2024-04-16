# Generated by Django 5.0.3 on 2024-04-02 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TogriSoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NotogriSoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=255)),
                ('togriSoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.togrisoz')),
            ],
        ),
    ]
