# Generated by Django 4.1.1 on 2023-04-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_kochi_fare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jaipur_fare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=30)),
                ('Mansarovar', models.CharField(max_length=5)),
                ('New_Aatish_Market', models.CharField(max_length=5)),
                ('Vivek_Vihar', models.CharField(max_length=5)),
                ('Shayam_Nagar', models.CharField(max_length=5)),
                ('Ram_Nagar', models.CharField(max_length=5)),
                ('Civil_Lines', models.CharField(max_length=5)),
                ('Jaipur_Metro_Station', models.CharField(max_length=5)),
                ('Sindhi_Camp', models.CharField(max_length=5)),
                ('Chandpole', models.CharField(max_length=5)),
                ('Chhoti_Chaupar', models.CharField(max_length=5)),
                ('Badi_Chaupar', models.CharField(max_length=5)),
            ],
        ),
    ]
