from django.db import models


class Data(models.Model):
    """Модель таблицы с данными занятости города."""

    vneshnij_identifikator_dlja_importa = models.CharField(
        max_length=255, verbose_name='город'
        )
    familija = models.CharField(max_length=255, verbose_name='фамилия')
    imja = models.TextField(max_length=255, verbose_name='имя')
    otchestvo = models.TextField(max_length=255, verbose_name='отчество')
    otdel = models.TextField(max_length=255, verbose_name='отдел')
    dolzhnost = models.TextField(max_length=255, verbose_name='должность')
    adres_elektronnoj_pochty = models.TextField(
        max_length=255, null=True, default=None,
        verbose_name='адрес электронной почты'
        )
    mobilnyj_telefon = models.TextField(
        max_length=255, null=True, default=None,
        verbose_name='мобильный телефон'
        )
    gorodskoj_telefon = models.TextField(
        max_length=255, null=True, default=None,
        verbose_name='городской телефон'
        )
    vnutrennij_telefon = models.TextField(
        max_length=255, verbose_name='внутренний телефон'
        )
    domashnij_telefon = models.TextField(
        max_length=255, null=True, default=None,
        verbose_name='домашний телефон'
        )
    login = models.TextField(
        max_length=255, null=True, default=None, verbose_name='логин'
        )
    parol = models.TextField(
        max_length=255, null=True, default=None, verbose_name='пароль'
        )

    def __str__(self):
        return self.familija

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
