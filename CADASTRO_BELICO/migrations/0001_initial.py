# Generated by Django 4.2.3 on 2023-07-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroArma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(max_length=8, verbose_name='NÚMERO DE SÉRIE')),
                ('tipo', models.IntegerField(choices=[(1, 'PISTOLA'), (2, 'ARMA LONGA')], verbose_name='TIPO')),
                ('modelo', models.IntegerField(choices=[(1, 'PT 100'), (2, 'SMT'), (3, 'CT')], verbose_name='MODELO')),
            ],
            options={
                'verbose_name': 'Cadastro de Arma',
                'verbose_name_plural': 'Cadastro de Armas',
            },
        ),
        migrations.CreateModel(
            name='CadastroColete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerocad', models.CharField(max_length=20, verbose_name='NÚMERO DE SÉRIE')),
                ('tamanho', models.IntegerField(choices=[(1, 'P'), (2, 'M'), (3, 'G'), (4, 'GG')], verbose_name='TAMANHO')),
                ('fabricante', models.CharField(max_length=20, verbose_name='FABRICANTE')),
            ],
            options={
                'verbose_name': 'Cadastro de Colete',
                'verbose_name_plural': 'Cadastro de Coletes',
            },
        ),
        migrations.CreateModel(
            name='Carregador_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_serie_1', models.CharField(max_length=8, verbose_name='NÚMERO DE SÉRIE')),
                ('qtd_carreg_1', models.IntegerField(verbose_name='QUANTIDADE DE MUNIÇÃO')),
            ],
            options={
                'verbose_name': 'Cadastro de Carregador_1',
                'verbose_name_plural': 'Cadastro de Carregadores_1',
            },
        ),
        migrations.CreateModel(
            name='Carregador_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_serie_2', models.CharField(max_length=8, verbose_name='NÚMERO DE SÉRIE')),
                ('qtd_carreg_2', models.IntegerField(verbose_name='QUANTIDADE DE MUNIÇÃO')),
            ],
            options={
                'verbose_name': 'Cadastro de Carregador_2',
                'verbose_name_plural': 'Cadastro de Carregadores_2',
            },
        ),
        migrations.CreateModel(
            name='Carregador_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_serie_3', models.CharField(max_length=8, verbose_name='NÚMERO DE SÉRIE')),
                ('qtd_carreg_3', models.IntegerField(verbose_name='QUANTIDADE DE MUNIÇÃO')),
            ],
            options={
                'verbose_name': 'Cadastro de Carregador_3',
                'verbose_name_plural': 'Cadastro de Carregadores_3',
            },
        ),
    ]