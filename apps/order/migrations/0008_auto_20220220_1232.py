# Generated by Django 3.2.12 on 2022-02-20 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0007_auto_20220219_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_placed_at',
            new_name='created_at',
        ),
        migrations.CreateModel(
            name='OrderActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('system_generated_comment', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_logs', to='order.order')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
