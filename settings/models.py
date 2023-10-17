from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    facebook_url = models.URLField(
        verbose_name="Ссылка на Facebook"
    )
    instagram_url = models.URLField(
        verbose_name="Ссылка на Instagram"
    )
    linkeldin_url = models.URLField(
        verbose_name="Ссылка на Linkeldin"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройка"


class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="имя пользоветеля"
    )
    email = models.EmailField(
        verbose_name="почта"
    )
    message = models.TextField(
        verbose_name="сообщении"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= "Обратная связ"
        verbose_name_plural = "обратные связи"