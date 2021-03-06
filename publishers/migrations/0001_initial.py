# Generated by Django 3.2.7 on 2021-09-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_sinhala', models.CharField(default=' ', max_length=250)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='publishers/logo')),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('land_tel', models.CharField(blank=True, default='', max_length=11, null=True)),
                ('tel1', models.CharField(blank=True, default='', max_length=11, null=True)),
                ('tel2', models.CharField(blank=True, default='', max_length=11, null=True)),
            ],
        ),
    ]
