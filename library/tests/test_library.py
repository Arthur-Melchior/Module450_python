from django.test import TestCase, Client
from django.urls import reverse
from library.models import Book
from unittest.mock import patch

class BookIntegrationTest(TestCase):

    def test_create_book(self):
        # Arrange : Données du nouveau livre à créer
        new_book_data = {'title': 'Pico Bogue', 'author': 'Dominique Roques'}

        # Act : Envoi d'une requête POST pour créer un nouveau livre
        client = Client()
        response = client.post(reverse('create_book'), data=new_book_data)

        # Assert
        # Redirection vers la page de détail du livre après sa création
        self.assertRedirects(response, reverse('info', args=[1]), status_code=302, target_status_code=200)
        # Livre créé correctement dans la BD
        book = Book.objects.get(id=1)
        assert book.author == "Dominique Roques"
        assert book.title == "Pico Bogue"

    def test_get_books(self):
        # Arrange : Création de quelques livres de test
        Book.objects.create(title='Book 1', author='Author 1')

        # Act : Envoi d'une requête GET pour obtenir la liste de tous les livres
        client = Client()
        response = client.get(reverse('all_books'))

        # Assert
        self.assertEqual(response.status_code, 200)  # Vérifier si la requête a réussi
        self.assertTemplateUsed(response, 'all_books.html')  # Vérifier si le bon template est utilisé


# def test_quit_directly_without_infinite_loop(mocker):
#     # arrange
#     controller = Controller()
#     with patch.object(View, 'get_user_input', return_value='5') as mock_get_input:
#         # act
#         controller.run()
#         # assert
#         mock_get_input.assert_called_once_with("Enter your choice")
