# Generated by Django 3.2 on 2021-06-05 12:51

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('uui', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('phonePrefix', models.CharField(blank=True, max_length=5, null=True, verbose_name='Prefijo')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
