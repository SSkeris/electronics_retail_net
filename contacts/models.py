from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    """Модель контакта."""
    email = models.EmailField(unique=True, verbose_name="email", help_text="email address")
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='номер дома', **NULLABLE)

    def __str__(self):
        return f"{self.email} - {self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
