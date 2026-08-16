from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id',        models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city',      models.CharField(max_length=100)),
                ('state',     models.CharField(max_length=100)),
                ('zip',       models.CharField(blank=True, default='', max_length=20)),
                ('address',   models.CharField(blank=True, default='', max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('phone',     models.CharField(blank=True, default='', max_length=50)),
            ],
            options={'verbose_name': 'Dealer', 'verbose_name_plural': 'Dealers'},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id',            models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',          models.CharField(max_length=100)),
                ('review',        models.TextField()),
                ('purchase',      models.BooleanField(default=False)),
                ('purchase_date', models.CharField(blank=True, default='', max_length=50)),
                ('car_make',      models.CharField(blank=True, default='', max_length=100)),
                ('car_model',     models.CharField(blank=True, default='', max_length=100)),
                ('car_year',      models.IntegerField(default=2023)),
                ('dealer',        models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='reviews',
                    to='djangoapp.dealer'
                )),
            ],
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
