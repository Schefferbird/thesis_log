# Generated by Django 2.0.10 on 2019-02-06 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20190206_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='author',
            field=models.ForeignKey(default='rs222vt', on_delete=django.db.models.deletion.PROTECT, related_name='logs', to='log.Author'),
        ),
    ]
