# Generated by Django 3.1.14 on 2022-06-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.EmailField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
