
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel


class PromotionalCode(BaseModel):

    class YearInSchool(models.TextChoices):
        PERCENTAGE = 'PERC', _('Porcentaje')
        FIXED_AMOUNT = 'FIXED', _('Cantidad fija')
        FREE = 'FREE', _('Gratis')

    name = models.CharField(
        _('Nombre de la promoción'),
        max_length=100
    )

    code = models.CharField(
        _('Código de la promoción'),
        max_length=30,
        unique=True
    )

    cart_discount = models.TextField(
        _('Tipo de descuento'),
        max_length=6,
        choices=YearInSchool.choices,
        default=YearInSchool.PERCENTAGE
    )

    discount_mount = models.IntegerField(
        _('Porcentaje o cantidad de descuento'),
        default=0,
    )

    expiry_datetime = models.DateTimeField(
        _('Fecha y hora de vencimiento')
    )

    max_uses = models.IntegerField(
        _('Máximo de usos'),
        default=10,
    )

    uses_count = models.IntegerField(
        _('Veces usado'),
        default=0
    )

    is_active = models.BooleanField(
        _('Promoción válida'),
        default=True,
    )

    def update_use(self):
        self.uses_count += 1
        if self.uses_count >= self.max_uses:
            self.is_active = False
        self.save()

    def __str__(self):
        return f'{self.code} - {self.name}'

    class Meta:
        verbose_name = _('Código promocional')
        verbose_name_plural = _('Códigos promocionales')
