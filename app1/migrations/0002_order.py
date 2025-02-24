# Generated by Django 5.0.7 on 2024-07-29 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_scoops', models.PositiveIntegerField()),
                ('icecream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app1.icecream')),
            ],
        ),
    ]
