# Generated by Django 2.1.7 on 2019-03-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0004_auto_20190316_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskassign',
            name='cost',
        ),
        migrations.AddField(
            model_name='taskassign',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project_manager.Employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskassign',
            name='status',
            field=models.CharField(choices=[('1', 'Completed'), ('2', 'Processing'), ('3', 'Failed')], default='2', max_length=1),
        ),
    ]
