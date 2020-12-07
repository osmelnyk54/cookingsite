from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    recept_day = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    is_day = models.BooleanField(default=False)
    is_holiday = models.BooleanField(default=False)
    is_health = models.BooleanField(default=False)
    is_modelss = models.BooleanField(default=False)
    is_equipment = models.BooleanField(default=False)
    is_thematic = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
