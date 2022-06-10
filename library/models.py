from django.db import models
from django.forms import FileField

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=80)
    def __init__():
        return

class ClassLevel(models.Model):
    level = models.CharField(max_length=80)
    def __init__():
        return

class BookClassification(models.Model):
    classification = models.CharField(max_length=50)
    def __init__():
        return

class Book(models.Model):
    book_classification = models.ForeignKey(BookClassification, on_delete=models.CASCADE)
    level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='bookCover/%Y/%m/%d/', max_length=None)
    pdf = models.FileField(upload_to='bookFiles/%Y/%m/%d/', max_length=None)
    video = models.FileField(upload_to='bookFiles/%Y/%m/%d/', max_length=None)
    book_title = models.CharField(max_length=150)
    page_count = models.CharField(default=">5")
    date_added = models.DateField(auto_now=True)

    def __init__(self):
        return
    def __unicode__(self):
        return
    def __str__(self):
        return "{}, {}" .format(self.book_title, self.author)

    def create_book(self):
        return