from django.db import models
from category.models import Category

class Booklist(models.Model):


    add = models.ForeignKey(Category)
    image_url = models.CharField(max_length=200, blank=True, default="")
    title = models.TextField(blank=True, default="")
    isbn = models.TextField(blank=True, default="")
    download = models.TextField(blank=True, default="")


    added_on = models.DateTimeField('date added')

    def __unicode__(self):
        return '%s' % (self.title)
        return '%s' % (self.image_url)
        return '%s' % (self.isbn)
        return '%s' % (self.download)
