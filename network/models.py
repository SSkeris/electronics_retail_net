from django.db import models
from contacts.models import Contact
from products.models import Product

NULLABLE = {'blank': True, 'null': True}


class NetworkNode(models.Model):
    """Звено торговой сети."""

    LEVELS = [
        (0, 'Производитель'),
        (1, 'Дистрибьютор / Продавец'),
        (2, 'Продавец'),
    ]

    level = models.IntegerField(choices=LEVELS)
    title = models.CharField(max_length=100, unique=True, verbose_name='название')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакт', **NULLABLE)
    products = models.ManyToManyField(Product, verbose_name='продукция')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='поставщик',
                                 verbose_name='поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления записи', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'звено торговой сети'
        verbose_name_plural = 'звенья торговой сети'
