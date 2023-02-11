from django.db import models
from author.decorators import with_author
from django.core.validators import MinLengthValidator
from django_cpf_cnpj.fields import CPFField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from main.utils import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, phone, first_name, last_name=None, password=None):
        """
        Creates and saves a User with the given phone, name and password.
        """
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone, first_name, password, last_name=None):
        """
        Creates and saves a staff user with the given phone, name and password.
        """
        user = self.create_user(
            phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, first_name, password, last_name=None):
        """
        Creates and saves a superuser with the given phone, name and password.
        """
        user = self.create_user(
            phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        verbose_name="Primeiro nome",
        max_length=64
    )
    last_name = models.CharField(
        verbose_name="Sobrenome",
        max_length=64,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True,
        unique=True
    )
    phone = models.CharField(max_length=13, verbose_name="Telefone", unique=True)
    cpf = CPFField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # a admin user; non super-user
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    # Email & Password are required by default.
    REQUIRED_FIELDS = ["first_name"]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_superuser(self):
        "Is the user a admin member?"
        return self.admin

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


@with_author
class UserAddress(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    zip_code = models.CharField(
        max_length=9,
        validators=[MinLengthValidator(8)],
        verbose_name="CEP"
    )
    country = models.CharField(
        max_length=128,
        verbose_name="País"
    )
    address = models.CharField(
        max_length=128,
        verbose_name="Endereço"
    )
    number = models.CharField(
        max_length=8,
        verbose_name="Número"
    )
    complement = models.CharField(
        max_length=256,
        verbose_name="Complemento",
        null=True,
        blank=True
    )
    neighborhood = models.CharField(
        max_length=128,
        verbose_name="Bairro"
    )
    city = models.CharField(
        max_length=128,
        verbose_name="Cidade"
    )
    state = models.CharField(
        max_length=2,
        validators=[MinLengthValidator(2)],
        verbose_name="Estado"
    )

    class Meta:
        verbose_name = "Endereço do usuário"
        verbose_name_plural = "Endereços dos usuários"

    def __str__(self) -> str:
        return f"{self.user} - {self.address}, {self.number}"
