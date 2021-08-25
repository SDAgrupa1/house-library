from django.test import TestCase

from .models import Music

"""To run all tests type python manage.py test music"""


class MusicModelTest(TestCase):

    def test_string_representation_for_performer(self):
        music = Music(performer="Madonna")
        self.assertEqual(str(music), music.performer)

    def test_string_representation_for_name_cd(self):
        music = Music(name_cd="Like a Prayer")
        self.assertEqual(str(music), music.name_cd)

    def test_string_representation_for_publisher(self):
        music = Music(publisher="Sire Records")
        self.assertEqual(str(music), music.publisher)
