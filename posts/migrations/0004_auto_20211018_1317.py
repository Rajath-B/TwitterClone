# Generated by Django 3.2.8 on 2021-10-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=148, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=24, verbose_name='Name'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]
