# Generated by Django 2.2 on 2019-04-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('middleName', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('M', 'Man'), ('W', 'Women')], default='M', max_length=1)),
                ('birth_date', models.DateTimeField(verbose_name='BirthDate')),
                ('results', models.ManyToManyField(to='clinic.Result')),
            ],
        ),
    ]