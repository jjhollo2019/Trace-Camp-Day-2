# Generated by Django 2.1.4 on 2019-01-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KickStarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backer_count', models.IntegerField()),
                ('blurb', models.TextField()),
                ('category', models.TextField()),
                ('converted_pledged_amount', models.FloatField()),
            ],
        ),
    ]
