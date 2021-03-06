# Generated by Django 3.1 on 2020-08-28 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapno', models.IntegerField()),
                ('blueprint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='maps.blueprint')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='maps.stage')),
            ],
        ),
    ]
