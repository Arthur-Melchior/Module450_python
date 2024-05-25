from django.test import TestCase
from library.models import Book

class BookUnitTest(TestCase):
    fixtures = ['books_fixture.json']  # Charger la fixture

    def test_get_book_details(self):
        # Récupérer le premier livre de fixture
        book = Book.objects.get(pk=1)

        # Act : Appel de la méthode get_book_details
        details = book.get_book_details()

        # Assert : Vérifier que les détails retournés sont corrects
        self.assertEqual(details['title'], 'Book 1')
        self.assertEqual(details['author'], 'Author 1')
