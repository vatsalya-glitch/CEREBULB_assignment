# Generated by Django 3.1.5 on 2021-01-25 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.IntegerField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_code', models.IntegerField(max_length=10)),
                ('product_img', models.FilePathField(path='/img')),
                ('product_mfc_date', models.DateField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.category')),
            ],
        ),
    ]