# Generated by Django 3.0.8 on 2020-07-31 00:02

from django.db import migrations, models
import django.db.models.deletion
import milksky.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geotiff', models.FileField(upload_to='')),
                ('designator', models.CharField(max_length=50)),
                ('satellite', models.CharField(max_length=50)),
                ('resolutionInMeters', models.DecimalField(decimal_places=2, max_digits=5)),
                ('region', models.CharField(max_length=50)),
                ('dateTimeOfCapture', models.DateTimeField()),
                ('humanPresenceLevel', models.IntegerField(validators=[milksky.models.validateScale1to10])),
                ('interestLevel', models.IntegerField(validators=[milksky.models.validateScale1to10])),
                ('cloudCoverage', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('nextPoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='milksky.Point')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taggedName', models.CharField(max_length=50)),
                ('predictedName', models.CharField(max_length=50)),
                ('percentOfTile', models.DecimalField(decimal_places=2, max_digits=5)),
                ('firstPoint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='milksky.Point')),
                ('tile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milksky.Tile')),
            ],
        ),
        migrations.CreateModel(
            name='Delta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentLandChange', models.DecimalField(decimal_places=2, max_digits=5)),
                ('designator', models.CharField(max_length=50)),
                ('newDateTime', models.DateTimeField()),
                ('oldDateTime', models.DateTimeField()),
                ('previousDelta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='milksky.Delta')),
            ],
        ),
    ]
