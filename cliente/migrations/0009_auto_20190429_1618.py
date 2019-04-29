# Generated by Django 2.2 on 2019-04-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0008_telefone_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cpf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11)),
                ('data_exp', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.OneToOneField(blank=True, null=True, on_delete=True, to='cliente.Cpf'),
        ),
    ]
