# Generated by Django 3.2.12 on 2022-03-07 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0002_initial'),
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('issue', 'Issue'), ('delivered', 'Delivered')], default='pending', max_length=40, verbose_name='Publisher package status')),
                ('order_window', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='order.orderwindow', verbose_name='Order window')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publisher_packages', to='publisher.publisher', verbose_name='Publisher')),
                ('related_orders', models.ManyToManyField(related_name='publisher_related_orders', to='order.Order', verbose_name='Publisher related order')),
            ],
            options={
                'verbose_name': 'Publisher Package',
                'verbose_name_plural': 'Publisher packages',
                'unique_together': {('publisher', 'order_window')},
            },
        ),
        migrations.CreateModel(
            name='SchoolPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_transit', 'In transit'), ('issue', 'Issue'), ('delivered', 'Delivered')], default='pending', max_length=40, verbose_name='School package status')),
                ('order_window', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='order.orderwindow', verbose_name='Order window')),
                ('related_orders', models.ManyToManyField(related_name='school_related_orders', to='order.Order', verbose_name='School related order')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='school_packages', to=settings.AUTH_USER_MODEL, verbose_name='School')),
            ],
            options={
                'verbose_name': 'School Package',
                'verbose_name_plural': 'School packages',
                'unique_together': {('school', 'order_window')},
            },
        ),
        migrations.CreateModel(
            name='SchoolPackageBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='school_package_book', to='book.book', verbose_name='Book')),
                ('school_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='school_package', to='package.schoolpackage', verbose_name='School package')),
            ],
            options={
                'verbose_name': 'School package related book',
                'verbose_name_plural': 'School package related books',
            },
        ),
        migrations.CreateModel(
            name='PublisherPackageBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publisher_package_book', to='book.book', verbose_name='Book')),
                ('publisher_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publisher_package', to='package.publisherpackage', verbose_name='Publisher package')),
            ],
            options={
                'verbose_name': 'Publisher package related book',
                'verbose_name_plural': 'Publisher related books',
            },
        ),
        migrations.CreateModel(
            name='CourierPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_transit', 'In transit'), ('issue', 'Issue'), ('delivered', 'Delivered')], default='pending', max_length=40, verbose_name='Courier package status')),
                ('order_window', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='order.orderwindow', verbose_name='Order window')),
                ('related_orders', models.ManyToManyField(related_name='courier_related_orders', to='order.Order', verbose_name='School related order')),
                ('school_package_books', models.ManyToManyField(related_name='courier_school_package_books', to='package.SchoolPackageBook', verbose_name='School package books')),
            ],
            options={
                'verbose_name': 'Courier Package',
                'verbose_name_plural': 'Courier Packages',
            },
        ),
    ]
