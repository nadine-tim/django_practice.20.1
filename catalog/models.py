from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание', **NULLABLE)
    img = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена')
    data_create = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    data_edit = models.DateTimeField(verbose_name='Дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание', **NULLABLE)
    # created_at = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    version_number = models.PositiveIntegerField(default=0, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    is_activ = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        # Строковое отображение объекта
        return f'Версия {self.version_number}: {self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
