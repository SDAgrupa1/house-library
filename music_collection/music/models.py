from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    BLUES = "Blues"
    CLASSICAL = "Classical"
    COUNTRY = "Country"
    DISCO_POLO = "Disco-Polo"
    ELECTRONIC = "Electronic"
    JAZZ = "Jazz"
    METAL = "Metal"
    POP = "Pop"
    RB = "R&B"
    RAP = "Rap"
    REAGGAE = "Reaggae"
    ROCK = "Rock"
    SOUNDTRACK = "Soundtrack"
    TRIPHOP = "Triphop"

    CATEGORY_CHOOSE = [
        (BLUES, "Blues"),
        (CLASSICAL, "Classical"),
        (COUNTRY, "Country"),
        (DISCO_POLO, "Disco-Polo"),
        (ELECTRONIC, "Electronic"),
        (JAZZ, "Jazz"),
        (METAL, "Metal"),
        (POP, "Pop"),
        (RB, "R&B"),
        (RAP, "Rap"),
        (REAGGAE, "Reaggae"),
        (ROCK, "Rock"),
        (SOUNDTRACK, "Soundtrack"),
        (TRIPHOP, "Triphop"),
    ]
    category_choose = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOOSE,
        unique=True,
        null=True
    )

    @property
    def is_upperclass(self):
        return self.category_choose in {self.CATEGORY_CHOOSE}

    def __str__(self):
        return f'{self.category_choose}'


class Availability(models.Model):
    AVAILABLE = "Available"
    BORROWED = "Borrowed"

    AVAILABILITY_CHOICES = [
        (AVAILABLE, "Available"),
        (BORROWED, "Borrowed"),
    ]
    availability_choices = models.CharField(
        max_length=50,
        choices=AVAILABILITY_CHOICES,
        unique=True,
        null=True
    )

    def is_upperclass(self):
        return self.availability_choices in {self.AVAILABILITY_CHOICES}

    def __str__(self):
        return f'{self.availability_choices}'


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
