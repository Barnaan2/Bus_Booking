# Generated by Django 4.0.6 on 2022-08-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_admin', '0001_initial'),
        ('bus_admin', '0005_remove_route_bus_subroute_bus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subroute',
            name='bus',
            field=models.ManyToManyField(null=True, related_name='single_route_bus', to='system_admin.bus'),
        ),
    ]