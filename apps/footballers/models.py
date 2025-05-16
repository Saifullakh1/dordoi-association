import uuid
from django.db import models
from django.utils.text import slugify


class PositionChoice(models.TextChoices):
    goalkeeper = 'Вратарь'
    defender = 'Защитник'
    midfielder = 'Полузащитник'
    forward = 'Нападающий'


class CitizenshipChoice(models.TextChoices):
    kyrgyz = 'Кыргызское'
    russian = 'Российское'
    kazakh = 'Казахское'
    brazilian = 'Бразильское'


class Footballer(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    image = models.FileField(upload_to='footballer', verbose_name="Фото")
    birthday = models.DateField(verbose_name="День рождения")
    number = models.IntegerField(default=0, verbose_name="Игровой номер")
    height = models.IntegerField(default=0, verbose_name="Рост")
    weight = models.IntegerField(default=0, verbose_name="Вес")
    citizenship = models.CharField(max_length=255, choices=CitizenshipChoice.choices, verbose_name="Гражданство")
    position = models.CharField(max_length=155, choices=PositionChoice.choices, verbose_name="Позиция")
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name="Слаг")

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.full_name)
            try:
                obj = Footballer.objects.get(slug=slug)
                slug += "-" + str(uuid.uuid4().hex[:4])
            except Footballer.DoesNotExist:
                pass
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"
        ordering = ('-id', )

    def __str__(self):
        return self.full_name