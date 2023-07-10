from django.db import models

class CadastroArma(models.Model):

    TIPO_CHOICES = [
        (1, 'PISTOLA'),
        (2, 'ARMA LONGA'),
    ]

    MODELO_CHOICES = [
        (1, 'PT 100'),
        (2, 'SMT'),
        (3, 'CT'),  
    ]

    numero_serie = models.CharField('NÚMERO DE SÉRIE', max_length=8)
    tipo = models.IntegerField(verbose_name='TIPO', choices=TIPO_CHOICES)
    modelo = models.IntegerField(verbose_name='MODELO', choices=MODELO_CHOICES)

    def __str__(self):
        return str(self.numero_serie)

    class Meta:
        verbose_name = 'Cadastro de Arma'
        verbose_name_plural = 'Cadastro de Armas'


class Carregador_1(models.Model):

    num_serie_1 = models.CharField('NÚMERO DE SÉRIE', max_length=8)
    qtd_carreg_1 = models.IntegerField(verbose_name='QUANTIDADE DE MUNIÇÃO')
    
    def __str__(self):
        return str(self.num_serie_1)

    class Meta:
        verbose_name = 'Cadastro Carregador 1'
        verbose_name_plural = 'Cadastro Carregadores 1'


class Carregador_2(models.Model):

    num_serie_2 = models.CharField('NÚMERO DE SÉRIE', max_length=8)
    qtd_carreg_2 = models.IntegerField(verbose_name='QUANTIDADE DE MUNIÇÃO')
    
    def __str__(self):
        return str(self.num_serie_2)

    class Meta:
        verbose_name = 'Cadastro Carregador 2'
        verbose_name_plural = 'Cadastro Carregadores 2'


class Carregador_3(models.Model):

    num_serie_3 = models.CharField('NÚMERO DE SÉRIE', max_length=8)
    qtd_carreg_3 = models.IntegerField(verbose_name='QUANTIDADE DE MUNIÇÃO')
    
    def __str__(self):
        return str(self.num_serie_3)

    class Meta:
        verbose_name = 'Cadastro Carregador 3'
        verbose_name_plural = 'Cadastro Carregadores 3'


class CadastroColete(models.Model):
    TAMANHO_COICHES = [
        (1, 'P'),
        (2, 'M'),
        (3, 'G'),
        (4, 'GG'),
     ]

    numerocad = models.CharField('NÚMERO DE SÉRIE', max_length=20)
    tamanho = models.IntegerField(verbose_name='TAMANHO', choices=TAMANHO_COICHES)
    fabricante = models.CharField('FABRICANTE', max_length=20)

    def __str__(self):
        return str(self.numerocad)

    class Meta:
        verbose_name = 'Cadastro de Colete'
        verbose_name_plural = 'Cadastro de Coletes'