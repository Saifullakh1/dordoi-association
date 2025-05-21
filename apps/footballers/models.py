import uuid
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from datetime import timedelta



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
    is_active = models.BooleanField(default=True, verbose_name="Активный")

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
    

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.FileField(upload_to='banner', verbose_name='Фото')

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ('-id', )
    def __str__(self):
        return self.title


# models.py

from django.db import models
from django.utils import timezone




class StoryMedia(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    
    story = models.ForeignKey('Stories', related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='storiesPage/media/')
    order = models.PositiveIntegerField(default=0, help_text="Order of media item in the story")

    class Meta:
        verbose_name = "Медиа сториса"
        verbose_name_plural = "Медиа сторисов"
        ordering = ['order']

    def __str__(self):
        return f"{self.media_type} for {self.story.title}"

class Stories(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="storiesPage/thumbnails/", blank=True, null=True)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def isNew(self):
        """Returns True if the story was created within the last 7 days."""
        return timezone.now().date() - self.date <= timezone.timedelta(days=7)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сторис"
        verbose_name_plural = "Сторисы"
        ordering = ['-date']