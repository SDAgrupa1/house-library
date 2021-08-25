from django.db import models

#model Category
class Category(models.Model):  # model 1 do 1 - 1 płycie będzie przyslugiwał 1 kategoria
    CATEGORY = {
        (0, "Rock"),
        (1, "Metal"),
        (2, "Blues"),
        (3, "Jazz"),
        (4, "Classical"),
        (5, "Country"),
        (6, "Electronic"),
        (7, "Pop"),
        (8, "R&B"),
        (9, "Rap"),
        (10, "Reaggae"),
        (11, "Soundtrack"),
        (12, "Triphop"),
    }


#model MUSIC
class Music(models.Model):
    performer = models.CharField(max_length=64, blank=False, unique=True)
    name_cd = models.CharField(max_length=64, blank=False)
    publisher = models.CharField(max_length=64, blank=False)
    year = models.DateField(null=True, blank=True)
    # rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    info = models.TextField(default="")
    category_models = models.OneToOneField(Category, on_delete=models.CASCADE, null=True, blank=True)
