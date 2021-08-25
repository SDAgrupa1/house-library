from django.db import models


#model MUSIC
class Music(models.Model):
    performer = models.CharField(max_length=64, blank=False, unique=True)
    name_cd = models.CharField(max_length=64, blank=False)
    publisher = models.CharField(max_length=64, blank=False)
    year = models.DateField(null=True, blank=True)
    # rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    info = models.TextField(default="")
    category_models = models.OneToOneField(Category, on_delete=models.CASCADE, null=True, blank=True)

