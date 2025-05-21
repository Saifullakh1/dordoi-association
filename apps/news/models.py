from django.db import models


class NewsType(models.TextChoices):
    university = 'University'
    football = 'Football'
    plaza = 'Plaza'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(upload_to="news_image", verbose_name="Картинка")
    type = models.CharField(max_length=255, choices=NewsType.choices)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-id', )

    def __str__(self):
        return f"{self.title}"
