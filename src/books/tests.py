from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .views import ListCreateBookAPIView, RetrieveUpdateDestroyBookAPIView
from .models import Book

list_books = [
    {
        "isbn": "9781593275846",
        "title": "Eloquent JavaScript, Second Edition",
        "author": "Marijn Haverbeke",
        "published_date": "2014-12-14",
        "pages": 472,
        "language": "English"
    },
    {
        "isbn": "9781449331818",
        "title": "Learning JavaScript Design Patterns",
        "author": "Addy Osmani",
        "published_date": "2012-07-01",
        "pages": 254,
        "language": "English"
    }
]

update_book_data = {
    "isbn": "9781449331818",
    "title": "Learning JavaScript Design Patterns",
    "author": "Addy Osmani",
    "language": "English"
}


class BookTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        Book.objects.create(**list_books[0])

    def test_create_book(self):
        view = ListCreateBookAPIView.as_view()
        creating_book = list_books[1]
        request = self.factory.post('/books/', creating_book, format='json')
        response = view(request)
        created_book_id = response.data.pop('id')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.get(id=created_book_id).title, creating_book['title'])

    def test_delete_book(self):
        view = RetrieveUpdateDestroyBookAPIView.as_view()
        instance_id = Book.objects.get().id
        request = self.factory.delete(f'/books/{instance_id}/')
        response = view(request, pk=instance_id)
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=instance_id)

    def test_get_one_book(self):
        view = RetrieveUpdateDestroyBookAPIView.as_view()
        instance_id = Book.objects.get().id
        request = self.factory.get(f'/books/{instance_id}/')
        response = view(request, pk=instance_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(isinstance(response.data, dict), True)

    def test_get_all_books(self):
        view = ListCreateBookAPIView.as_view()
        request = self.factory.get('/books/')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(isinstance(response.data["results"], list), True)

    def test_update_book(self):
        view = RetrieveUpdateDestroyBookAPIView.as_view()
        instance_id = Book.objects.get().id
        request = self.factory.put(f'/books/{instance_id}/', update_book_data, format='json')
        response = view(request, pk=instance_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get(id=instance_id).isbn, update_book_data['isbn'])
        self.assertEqual(Book.objects.get(id=instance_id).title, update_book_data['title'])
        self.assertEqual(Book.objects.get(id=instance_id).author, update_book_data['author'])
        self.assertEqual(Book.objects.get(id=instance_id).language, update_book_data['language'])
