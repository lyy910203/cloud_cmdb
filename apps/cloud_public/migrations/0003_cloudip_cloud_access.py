# Generated by Django 3.1.1 on 2020-09-27 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0002_auto_20200926_2301'),
        ('cloud_public', '0002_cloudip_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloudip',
            name='cloud_access',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cloud.cloudaccess', verbose_name='主机账户'),
        ),
    ]
