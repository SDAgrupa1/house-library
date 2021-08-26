from django.test import TestCase

from .models import Music

"""To run all tests type python manage.py test music"""


class MusicModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified object used by test methods
        Music.objects.create(performer="Madonna",
                             name_cd="Like a Prayer",
                             publisher="Sire Records",
                             year="1989-01-01",
                             info="This is some example track list",
                             category_models=None
                             )
