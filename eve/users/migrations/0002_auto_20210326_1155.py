# Generated by Django 3.1.7 on 2021-03-26 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '__first__'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='roles.roles'),
        ),
        migrations.AddField(
            model_name='users',
            name='password_hash',
            field=models.CharField(default='aaaaa', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
