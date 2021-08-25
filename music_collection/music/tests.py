from django.test import TestCase

from .models import Music

"""To run all tests type python manage.py test music"""


class MusicModelTest(TestCase):

    def test_string_representation_for_performer(self):
        music = Music(performer="Madonna")
        self.assertEqual(str(music), music.performer)
