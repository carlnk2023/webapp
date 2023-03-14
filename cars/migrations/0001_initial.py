# Generated by Django 4.0.2 on 2023-03-14 23:05

import cars.models
from django.db import migrations, models
import django.db.models.deletion
import owners.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('model_name_slug', models.SlugField(blank=True)),
                ('class_name', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Truck', 'Truck'), ('SUV', 'SUV'), ('Van', 'Van')], default='Standard', max_length=50)),
                ('price_per_day', models.PositiveIntegerField(default=0, verbose_name='Price per day')),
                ('number_of_seats', models.PositiveIntegerField(default=1)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual'), ('Both', 'Both')], default='Automatic', max_length=9, verbose_name='Type of transmission')),
                ('mileage_limit', models.CharField(choices=[('Limited', 'Limited'), ('Unlimited', 'Unlimited')], default='Limited', max_length=9, verbose_name='Mileage/Kilometres limit')),
                ('mileage', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Mileage/Kilometres')),
                ('inventory_available', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3)),
                ('model_image', models.ImageField(upload_to=cars.models.user_directory_path_cars, validators=[owners.validators.validate_file_size], verbose_name='Model image')),
                ('bags', models.PositiveIntegerField(default=0)),
                ('doors', models.PositiveIntegerField(default=0)),
                ('security_deposit', models.PositiveIntegerField(default=0)),
                ('min_days', models.PositiveIntegerField(default=0)),
                ('ratings', models.CharField(max_length=5)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='owners.owner')),
                ('pickup_location', models.ManyToManyField(to='cars.Location', verbose_name='Available pick-up locations')),
            ],
            options={
                'verbose_name': 'Car Category',
                'verbose_name_plural': 'Car Categories',
                'ordering': ('-date_created',),
            },
        ),
    ]
