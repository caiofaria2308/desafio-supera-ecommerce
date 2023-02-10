from autoslug import AutoSlugField
from django.db import models
from author.decorators import with_author
from django.utils.text import slugify

from main.utils import BaseModel


@with_author
class Product(BaseModel):
    name = models.CharField(
        max_length=256,
        verbose_name="Nome"
    )
    slug = AutoSlugField(
        verbose_name="Slug",
        populate_from="name",
        unique=True
    )
    description = models.TextField(
        verbose_name="Descrição",
        null=True,
        blank=True
    )
    price = models.FloatField(
        verbose_name="Preço"
    )
    score = models.IntegerField(
        verbose_name="Popularidade"
    )
    image = models.ImageField(
        verbose_name="Imagem representativa",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - R${self.price}"
