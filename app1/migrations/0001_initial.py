# Generated by Django 5.0.7 on 2024-07-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
