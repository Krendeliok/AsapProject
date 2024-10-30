from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import BookSerializer
from .models import Book
from .filters import BookFilter
from .pagination import BookPagination


class ListCreateBookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter


class RetrieveUpdateDestroyBookAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
