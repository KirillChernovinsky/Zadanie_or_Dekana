from django.db import models



class Product(models.Model):
    product_name = models.CharField(max_length=40, verbose_name='Название товара: ')
    product_categori = models.CharField(max_length=40, verbose_name='Категория товара: ')
    product_description = models.CharField(max_length=400, verbose_name='Описание товара: ')
    product_img = models.URLField()

    def __str__(self):
        return f'{self.product_name} {self.product_categori} {self.product_description} {self.product_img}'



