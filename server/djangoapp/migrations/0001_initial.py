from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('country_of_origin', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={'verbose_name': 'Car Make', 'verbose_name_plural': 'Car Makes'},
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('car_type', models.CharField(
                    choices=[
                        ('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon'),
                        ('COUPE', 'Coupe'), ('CONVERTIBLE', 'Convertible'),
                        ('TRUCK', 'Truck'), ('VAN', 'Van'), ('HATCHBACK', 'Hatchback'),
                    ],
                    default='SEDAN', max_length=20
                )),
                ('year', models.IntegerField(default=2023)),
                ('dealer_id', models.IntegerField(blank=True, null=True)),
                ('car_make', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='car_models',
                    to='djangoapp.carmake'
                )),
            ],
            options={'verbose_name': 'Car Model', 'verbose_name_plural': 'Car Models'},
        ),
    ]
