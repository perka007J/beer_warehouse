from django.db import models
from core.models import CommonInfo


class Company(CommonInfo):
    name = models.CharField('Nombre', max_length=50)
    tax_number = models.IntegerField('Código', unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Beer(CommonInfo):

    class Color(models.IntegerChoices):
        YELLO = 1
        BLACK = 2
        AMBER = 3
        BROWN = 4

    name = models.CharField('Nombre: ', max_length=50)
    abv = models.DecimalField('Volumén de Alcohol',
                              max_digits=5, decimal_places=2, default=0)
    is_filter = models.BooleanField('¿Está Filtrado?', default=False)
    color = models.SmallIntegerField(
        'Color', choices=Color.choices, default=Color.YELLO)
    image = models.ImageField(
        'Imagen', upload_to='beer', blank=True, null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='beers')

    class Meta:
        verbose_name = 'Beer'
        verbose_name_plural = 'Beers'
        ordering = ['-name']

    def __str__(self):
        return self.name


class SpecialIngredients(CommonInfo):
    name = models.CharField('Nombre', max_length=50)
    beers = models.ManyToManyField(
        Beer, blank=True, related_name='special_ingredients')

    class Meta:
        verbose_name = 'Sepecial Ingredient'
        verbose_name_plural = 'Special Ingredients'
        ordering = ['-name']

    def __str__(self):
        return self.name
