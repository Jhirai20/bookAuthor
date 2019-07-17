from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Author object: {self.name} ({self.id})>"
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    author = models.ManyToManyField(Author, related_name="Book") # make sure to lowercase the realted_name field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Book object: {self.title} ({self.id})>"