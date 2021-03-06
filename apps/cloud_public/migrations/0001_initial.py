# Generated by Django 3.1.1 on 2020-09-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloudIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField(choices=[(1, 'ECS'), (2, 'LB')], default=1, verbose_name='云商代码')),
                ('ip', models.GenericIPAddressField(db_index=True, verbose_name='ip')),
                ('mac', models.CharField(default='', max_length=50, verbose_name='mac')),
                ('type', models.IntegerField(choices=[(1, '私网'), (2, '公网')], default=1, verbose_name='IP类型')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_datetime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '公共IP',
                'verbose_name_plural': '公共IP',
                'db_table': 'cloud_ip',
            },
        ),
    ]
