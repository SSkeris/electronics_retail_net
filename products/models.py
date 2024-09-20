from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель продуктов."""

    name = models.CharField(max_length=100, unique=True, verbose_name='название продукта')
    model_name = models.CharField(max_length=100, verbose_name='название модели продукта', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок', **NULLABLE)

    def __str__(self):
        return f"{self.name} - {self.model_name} ({self.release_date})"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
