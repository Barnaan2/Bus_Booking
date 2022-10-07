# Generated by Django 4.1.1 on 2022-10-07 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bus_admin', '0001_initial'),
        ('system_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_date', models.DateField(null=True)),
                ('travel_begin_time', models.TimeField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bus_admin.bus')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='system_admin.city')),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bus_admin.route')),
                ('start', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_admin.city')),
                ('subroute_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bus_admin.subrouteadmin')),
            ],
        ),
    ]
