# Generated by Django 4.1.6 on 2023-02-10 00:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=64, verbose_name='Primeiro nome')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Sobrenome')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address')),
                ('phone', models.CharField(max_length=13, unique=True, verbose_name='Telefone')),
                ('cpf', django_cpf_cnpj.fields.CPFField(blank=True, max_length=14, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('zip_code', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='CEP')),
                ('country', models.CharField(max_length=128, verbose_name='País')),
                ('address', models.CharField(max_length=128, verbose_name='Endereço')),
                ('number', models.CharField(max_length=8, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=256, null=True, verbose_name='Complemento')),
                ('neighborhood', models.CharField(max_length=128, verbose_name='Bairro')),
                ('city', models.CharField(max_length=128, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Estado')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='useraddress_create', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='useraddress_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Endereço do usuário',
                'verbose_name_plural': 'Endereços dos usuários',
            },
        ),
    ]
