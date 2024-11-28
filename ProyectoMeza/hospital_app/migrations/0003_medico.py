# Generated by Django 5.1 on 2024-11-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0002_paciente_id_alter_paciente_id_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_medico', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
    ]