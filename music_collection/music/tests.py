from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import MusicAlbum, Performer

"""To run all tests type python manage.py test music"""


class MusicModelTest(TestCase):

    def setUp(self):
        # Set up non-modified object used by test methods

        performer = Performer.objects.create(name="Madonna",
                                             www='https: // www.madonna.com /'
                                             )

        MusicAlbum.objects.create(performer=performer,
                                  name_cd="Like a Prayer",
                                  publisher="Sire Records",
                                  year="1989",
                                  info="This is some example track list",
                                  category_models=None
                                  )

    # test for labels fields
    def test_performer_label(self):
        music = MusicAlbum.objects.get(id=1)
        field_label = music._meta.get_field("performer").verbose_name
        self.assertEqual(field_label, "performer")

    def test_name_cd_label(self):
        music = MusicAlbum.objects.get(id=1)
        field_label = music._meta.get_field("name_cd").verbose_name
        self.assertEqual(field_label, "name cd")

    def test_publisher_label(self):
        music = MusicAlbum.objects.get(id=1)
        field_label = music._meta.get_field("publisher").verbose_name
        self.assertEqual(field_label, "publisher")

    def test_year_label(self):
        music = MusicAlbum.objects.get(id=1)
        field_label = music._meta.get_field("year").verbose_name
        self.assertEqual(field_label, "year")

    def test_info_label(self):
        music = MusicAlbum.objects.get(id=1)
        field_label = music._meta.get_field("info").verbose_name
        self.assertEqual(field_label, "info")

    # test str representation
    def test_string_representation(self):
        music = MusicAlbum.objects.get(id=1)
        performer_field = music.performer
        name_cd_field = music.name_cd
        year_field = music.year
        self.assertEqual(str(music), f'{performer_field}: "{name_cd_field}", {year_field}')

    # test str in date field
    def test_str_in_year_should_fail(self):
        music = MusicAlbum(year="Two thousand ten")
        with self.assertRaises(ValueError):
            music.save()

    # test max len for performer field
    def test_performer_name_max_length(self):
        performer = Performer.objects.get(id=1)
        max_length = performer._meta.get_field('name').max_length
        self.assertEqual(max_length, 32)
