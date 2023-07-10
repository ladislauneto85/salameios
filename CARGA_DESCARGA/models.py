from django.db import models
from CADASTRO_POLICIAIS.models import User, CadastroPolicial
from CADASTRO_BELICO.models import CadastroArma, Carregador_1, Carregador_2, Carregador_3, CadastroColete

class Carga_Descarga(models.Model):

    PATENTE_CHOICES = [
        (1, 'CEL'),
        (2, 'TEN CEL'),
        (3, 'MAJ'),
        (4, 'CAP'),
        (5, 'TEN'),
        (6, 'ASP'),
        (7, 'SUB TEN'),
        (8, 'SGT'),
        (9, 'CB'),
        (10, 'SD'),
        (11, 'AL SD'),
    ]

    MUNICAO_CHOICES = [
        (1, '.40'),
        (2, '.556'),      
    ]

    cad_matricula = models.ForeignKey(CadastroPolicial, on_delete=models.CASCADE, verbose_name='MATRÍCULA')
    patente = models.IntegerField(verbose_name='POSTO/GRADUAÇÃO', choices=PATENTE_CHOICES)
    nomeguerra = models.CharField('NOME DE GUERRA', max_length=20)
    e_mail = models.ForeignKey(User, on_delete=models.CASCADE)
    armamento = models.ForeignKey(CadastroArma, on_delete=models.CASCADE, verbose_name='ARMA')
    carreg1 = models.ForeignKey(Carregador_1, on_delete=models.CASCADE, verbose_name='CARREGADOR 1')
    carreg2 = models.ForeignKey(Carregador_2, on_delete=models.CASCADE, verbose_name='CARREGADOR 2')
    carreg3 = models.ForeignKey(Carregador_3, on_delete=models.CASCADE, verbose_name='CARREGADOR 3')
    municao = models.IntegerField(verbose_name='MUNiÇÃO', choices=MUNICAO_CHOICES)
    placabalistica = models.ForeignKey(CadastroColete, on_delete=models.CASCADE, verbose_name='COLETE')
    observacao = models.CharField('OBSERVAÇÃO', max_length=50)    
    data = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return str(self.cad_matricula)

    class Meta:
        verbose_name = 'Carga_Descarga'
        verbose_name_plural = 'Cargas_Descargas'


