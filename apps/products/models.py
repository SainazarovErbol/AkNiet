import os
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from apps.categories.models import Category
from utils.image_path import upload_products


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='',
    )
    descriptions = RichTextField(
         verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='',
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание',
    )

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Продукт',
    )
    image = models.ImageField(
        upload_to=upload_products,
        verbose_name='Картинка',
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return f'{self.image.url}'
