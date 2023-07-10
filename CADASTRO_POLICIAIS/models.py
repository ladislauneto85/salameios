from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, nome_de_guerra, password=None):
        if not email:
            raise ValueError('Insira o email')

        user = self.model(
            email=self.normalize_email(email),
            nome_de_guerra=nome_de_guerra,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='E-MAIL',
        max_length=255,
        unique=True,
    )
    nome = models.CharField('NOME COMPLETO', max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Acesso'
        verbose_name_plural = 'Acessos'

# Importe a classe que apresentará um erro de validação
from django.core.exceptions import ValidationError

# Crie um método para validar o valor informado
def validate_matricula(value):
    if not value.isdigit():
        raise ValidationError('Deve conter apenas números')
    
class CadastroPolicial(models.Model):
    POSTOGRADUACAO_CHOICES = [
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

    matricula = models.CharField('MATRÍCULA', max_length=8, validators=[validate_matricula])
    nome_guerra = models.CharField('NOME DE GUERRA', max_length=50)
    posto_graduacao = models.IntegerField(verbose_name='POSTO/GRADUAÇÃO', choices=POSTOGRADUACAO_CHOICES)
    
    def __str__(self):
        return str(self.matricula)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'