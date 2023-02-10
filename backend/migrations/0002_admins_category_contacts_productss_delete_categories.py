# Generated by Django 4.1.2 on 2023-01-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Username', models.CharField(blank=True, max_length=25, null=True)),
                ('Password', models.CharField(blank=True, max_length=25, null=True)),
                ('Confirm', models.CharField(blank=True, max_length=25, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Brand', models.CharField(blank=True, max_length=25, null=True)),
                ('Description', models.CharField(blank=True, max_length=250, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Categry', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='categories',
        ),
    ]