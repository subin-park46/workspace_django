# Generated by Django 4.1.2 on 2022-10-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbtest2', '0002_alter_myboard_mytitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('mypassword', models.CharField(max_length=100)),
                ('myemail', models.CharField(max_length=100)),
            ],
        ),
    ]