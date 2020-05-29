from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField("Название", max_length=200,
                            db_index=True)
    slug = models.SlugField("Алиас продукта(его URL)", max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shops:product_list_by_category',
                           args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='Товары',
                                 on_delete=models.CASCADE)
    name = models.CharField("Название продукта", max_length=200, db_index=True)
    slug = models.SlugField("Алиас продукта(его URL)", max_length=200, db_index=True)
    image = models.ImageField("Изображение продукта", upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField("Описание продукта", blank=True)
    price = models.DecimalField("Десятичный тип для хранения десятичного числа с фиксированной точностью",
                                max_digits=10, decimal_places=2)
    available = models.BooleanField("Позволяет включить/отключить продукт в каталоге", default=True)
    created = models.DateTimeField("Это поле хранит дату когда был создан объект", auto_now_add=True)
    updated = models.DateTimeField("В этом поле хранится время последнего обновления объекта", auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shops:product_detail',
                           args=[self.id, self.slug])
