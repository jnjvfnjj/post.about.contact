from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
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
    logon = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройка"
        
# class About(models.Model):
#     descriptions = models.TextField(
#         verbose_name="Описание о нас"
#     )
    
#     def __str__(self):
#         return self.descriptions
    
#     class Meta:
#         verbose_name = "О нас"
#         verbose_name_plural = "О нас"
        
# class Teach(models.Model):
#     descriptions = models.TextField(
#         verbose_name="Описание о нас"
#     )
    
#     def __str__(self):
#         return self.descriptions
    
#     class Meta:
#         verbose_name = "Учеьная программа"
#         verbose_name_plural = "Учеьная программа"