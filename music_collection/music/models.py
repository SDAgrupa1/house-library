from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Category(models.Model):  # model 1 do 1 - 1 płycie będzie przyslugiwał 1 kategoria
    CATEGORY = {
        (0, "Blues"),
        (1, "Classical"),
        (2, "Country"),
        (3, "Disco-Polo"),
        (4, "Electronic"),
        (5, "Jazz"),
        (6, "Metal"),
        (7, "Pop"),
        (8, "R&B"),
        (9, "Rap"),
        (10, "Reaggae"),
        (11, "Rock"),
        (12, "Soundtrack"),
        (13, "Triphop"),
    }

    category = models.PositiveSmallIntegerField(default=0, choices=CATEGORY)

    def __str__(self):
        return f'{self.category}'


class Availability(models.Model):
    AVAILABLE = "A"
    BORROWED = "B"

    AVAILABILITY_CHOICES = [
        (AVAILABLE, "Available"),
        (BORROWED, "Borrowed"),
    ]
    availability_choices = models.CharField(
        max_length=1,
        choices=AVAILABILITY_CHOICES,
        unique=True,
        null=True
    )

    def is_upperclass(self):
        return self.availability_choices in {self.AVAILABILITY_CHOICES}


class Music(models.Model):
    performer = models.CharField(max_length=64, blank=False, unique=True)
    name_cd = models.CharField(max_length=64, blank=False)
    publisher = models.CharField(max_length=64, blank=False)
    year = models.DateField(null=True, blank=True)
    info = models.TextField(default="")
    category_models = models.OneToOneField(Category, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.ImageField(upload_to="covers", null=True, blank=True)
    availability = models.OneToOneField(Availability, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.performer} {self.name_cd}'


class Rating(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    music = models.ForeignKey(Music, null=True, default=None, related_name='ratings', on_delete=models.CASCADE,
                              blank=True)

    def __str__(self):
        return f'{self.stars} -> {self.review}'


