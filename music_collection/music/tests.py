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

    # test for labels fields
    def test_performer_label(self):
        music = Music.objects.get(id=1)
        field_label = music._meta.get_field("performer").verbose_name
        self.assertEqual(field_label, "performer")

    def test_name_cd_label(self):
        music = Music.objects.get(id=1)
        field_label = music._meta.get_field("name_cd").verbose_name
        self.assertEqual(field_label, "name cd")

    def test_publisher_label(self):
        music = Music.objects.get(id=1)
        field_label = music._meta.get_field("publisher").verbose_name
        self.assertEqual(field_label, "publisher")

    def test_year_label(self):
        music = Music.objects.get(id=1)
        field_label = music._meta.get_field("year").verbose_name
        self.assertEqual(field_label, "year")

    def test_info_label(self):
        music = Music.objects.get(id=1)
        field_label = music._meta.get_field("info").verbose_name
        self.assertEqual(field_label, "info")
