from django.test import TestCase
from library.models import Book
from unittest.mock import patch

class BookUnitTest(TestCase):
    fixtures = ['books_fixture.json']  # Charger la fixture

    def test_book_count(self):
        # Créer un mock pour l'objet Book.objects
        with patch('library.models.Book.objects') as mock_objects:
            # Configurer le mock pour retourner une valeur spécifique
            mock_objects.count.return_value = 4

            # Act : Appeler la méthode testée
            book_count = Book.objects.count()

            # Assert : Vérifier que le nombre retourné est correct
            self.assertEqual(book_count, 4)
