# Generated by Django 2.2 on 2019-04-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0012_auto_20190429_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
