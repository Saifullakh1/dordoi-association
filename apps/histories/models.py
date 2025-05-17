from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to='images', verbose_name="Картинка")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        ordering = ("-id", )

    def __str__(self):
        return f"{self.id}"


class History(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    images = models.ManyToManyField(Image, related_name="history_images", verbose_name="Картинки")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"
        ordering = ("-id", )

    def __str__(self):
        return self.title