from django.db import models
from course.models import Course

class Category(models.Model):



    category = models.ForeignKey(Course)
    title= models.TextField(blank=True, default="")
    totalbook = models.TextField(max_length=200, blank=True, default="")


    added_on = models.DateTimeField('date added')

    def __unicode__(self):

        return '%s' % (self.title)
        return '%s' % (self.totalbook)
