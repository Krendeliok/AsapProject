from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        indexes = [
            models.Index(fields=['author']),
            models.Index(fields=['published_date']),
            models.Index(fields=['language']),
        ]
