from django.db import models

from products.validators import validate_min_value


class Product(models.Model):
    """  Модель продукта. """
    name = models.CharField(max_length=200, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание', blank=True,
                                   null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена',
                                validators=[validate_min_value], blank=True,
                                null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
