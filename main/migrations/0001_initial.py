# Generated by Django 4.0.8 on 2023-04-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
                ('mnemonic', models.CharField(max_length=256)),
            ],
        ),
    ]
