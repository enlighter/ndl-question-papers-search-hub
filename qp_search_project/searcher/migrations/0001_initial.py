# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 13:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='search_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_month', models.DateField()),
                ('subject', models.CharField(max_length=45)),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='searcher.board')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searcher.exam')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('state', models.CharField(blank=True, choices=[('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('TG', 'Telangana'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chattisgarh'), ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'), ('UA', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Pondicherry')], max_length=21, null=True)),
                ('city', models.CharField(blank=True, max_length=21, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('educational_role', models.CharField(choices=[('vb', 'Till Class VIII'), ('mc', 'Class IX to X'), ('ss', 'Class XI to XII'), ('gr', 'UG or PG'), ('cd', 'Career Development or Technical Study'), ('ae', 'Adult Education'), ('ll', 'Lifelong Learner')], max_length=39)),
                ('institute', models.CharField(blank=True, max_length=99, null=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali')], max_length=8)),
            ],
        ),
    ]
