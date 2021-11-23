# Generated by Django 3.2.7 on 2021-11-18 15:23

import course.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(default='None')),
                ('doc_path', models.CharField(default='Documents', max_length=200)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='course.author')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('markdown', models.TextField()),
                ('html', models.TextField()),
                ('document', models.CharField(max_length=200)),
                ('book', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='course.book')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(default='book', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=course.models.get_upload)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='course.author')),
                ('chapter', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='course.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.image'),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]