from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(upload_to="news_image", verbose_name="Картинка")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.title}"
