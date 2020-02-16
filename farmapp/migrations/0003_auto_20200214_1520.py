# Generated by Django 3.0.3 on 2020-02-14 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0002_login_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bay_name', models.CharField(max_length=250)),
                ('qrcode', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_name', models.CharField(max_length=250)),
                ('qrcode', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vender_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tower_name', models.CharField(max_length=250)),
                ('tower_location', models.CharField(max_length=250)),
                ('qrcode', models.CharField(max_length=250)),
                ('tower_color', models.CharField(max_length=250)),
                ('tower_height', models.CharField(max_length=250)),
                ('Bay_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmapp.Bay')),
                ('Rack_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmapp.Rack')),
                ('vender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmapp.Vender')),
            ],
        ),
        migrations.AddField(
            model_name='bay',
            name='fk_rackid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmapp.Rack'),
        ),
    ]
