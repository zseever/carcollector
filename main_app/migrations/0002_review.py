# Generated by Django 4.1 on 2022-08-09 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.IntegerField()),
                ('desc', models.CharField(max_length=255)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
        ),
    ]