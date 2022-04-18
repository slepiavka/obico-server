# Generated by Django 2.1.7 on 2019-11-07 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20191107_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprint',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprinter',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprinter',
            name='action_on_failure',
            field=models.CharField(choices=[('NONE', 'Just notify me.'), ('PAUSE', 'Pause the printer and notify me.')], default='PAUSE', max_length=10),
        ),
        migrations.AlterField(
            model_name='printer',
            name='action_on_failure',
            field=models.CharField(choices=[('NONE', 'Just notify me.'), ('PAUSE', 'Pause the printer and notify me.')], default='PAUSE', max_length=10),
        ),
        migrations.AlterField(
            model_name='printer',
            name='current_print',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='not_used', to='app.Print'),
        ),
        migrations.DeleteModel(
            name='UserCredit',
        ),
    ]