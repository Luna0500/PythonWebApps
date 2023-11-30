# Generated by Django 4.2.4 on 2023-11-30 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperProfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('reporter', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SuperProfiles.reporter')),
            ],
        ),
    ]