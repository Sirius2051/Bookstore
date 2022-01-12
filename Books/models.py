from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, blank = True, null = True)
    author = models.CharField(max_length=255, blank = True, null = True)
    publication_date = models.DateField()
    gender = models.CharField(max_length=255, blank = True, null = True)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title
