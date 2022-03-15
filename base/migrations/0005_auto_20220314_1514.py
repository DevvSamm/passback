# Generated by Django 3.2 on 2022-03-14 14:14

import base.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220312_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='contact2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='hotel',
            name='cover',
            field=models.ImageField(default='hotel_placeholder.png', upload_to='cover/', verbose_name='image de couverture'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='identifiant',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='identifiant'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='lat',
            field=models.FloatField(blank=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='lng',
            field=models.FloatField(blank=True, verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=200, verbose_name="nom de l'hotel"),
        ),
        migrations.CreateModel(
            name='ImageHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=base.models.upload_directory, verbose_name='image')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Forfait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.IntegerField()),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.hotel')),
            ],
        ),
    ]