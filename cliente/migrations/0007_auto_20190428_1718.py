# Generated by Django 2.2 on 2019-04-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_auto_20190428_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produt',
            name='data',
            field=models.DateTimeField(),
        ),
    ]