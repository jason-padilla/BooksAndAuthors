from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Book object: {self.title} {self.description}>"
class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Author object: {self.first_name} {self.last_name} {self.books}>"