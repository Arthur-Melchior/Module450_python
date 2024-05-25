from django.test import TestCase, Client
from django.urls import reverse

class BookIntegrationTest(TestCase):
    fixtures = ['books_fixture.json']  # Charger la fixture

    def test_get_books(self):
        # Act : Envoi d'une requête GET pour obtenir la liste de tous les livres
        client = Client()
        response = client.get(reverse('all_books'))

        # Assert
        self.assertEqual(response.status_code, 200)  # Vérifier si la requête a réussi
        self.assertTemplateUsed(response, 'all_books.html')  # Vérifier si le bon template est utilisé

        # Vérifiez que les livres sont bien présents dans la réponse
        self.assertContains(response, 'Book 1')
        self.assertContains(response, 'Book 2')
        self.assertContains(response, 'Book 3')
        self.assertContains(response, 'Book 4')
