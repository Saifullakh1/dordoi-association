from django.db import models


class Club(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(upload_to="club_image", verbose_name="Картинка")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"
        ordering = ("-id", )

    def __str__(self):
        return self.title


class Match(models.Model):
    first_club = models.ForeignKey(Club, on_delete=models.CASCADE,
                                   related_name="first_club_match", verbose_name="Первый клуб"
                                   )
    second_club = models.ForeignKey(Club, on_delete=models.CASCADE,
                                    related_name="second_club_match", verbose_name="Второй клуб"
                                   )
    result = models.CharField(max_length=250, default="0:0", blank=True, null=True, verbose_name="Результат")
    date_at = models.DateField(blank=True, null=True, verbose_name="Дата матча")
    time_at = models.TimeField(blank=True, null=True, verbose_name="Время матча")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    location = models.CharField(max_length=255, verbose_name="Локация")
    championship = models.CharField(max_length=255, verbose_name="Чемпионат")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"
        ordering = ("-id", )

    def __str__(self):
        return f"{self.first_club.title} - {self.second_club.title}"

