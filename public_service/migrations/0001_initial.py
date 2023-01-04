# Generated by Django 4.1.4 on 2023-01-04 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birth', models.DateField()),
                ('e_mail', models.EmailField(max_length=250)),
                ('states', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espirírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=100)),
                ('marital_status', models.CharField(choices=[('not_married', 'Solteiro(a)'), ('married', 'Casado(a)'), ('divorced', 'Divorciado(a)'), ('widower', 'Viúvo(a)')], max_length=100)),
                ('average_wage', models.PositiveIntegerField()),
                ('schooling', models.CharField(choices=[('elemental school', 'Fundamental'), ('hight school', 'Medio'), ('college', 'Graduado')], max_length=250)),
                ('alive', models.CharField(choices=[('alive', 'Vivo'), ('dead', 'Morto')], max_length=100)),
            ],
        ),
    ]
