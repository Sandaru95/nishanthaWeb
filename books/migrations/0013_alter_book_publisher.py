# Generated by Django 3.2.7 on 2021-09-20 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
        ('books', '0012_auto_20210920_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publishers.publisher'),
        ),
    ]
