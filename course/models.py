from django.db import models

class Course(models.Model):


    title= models.TextField(blank=True, default="")
    image_url = models.CharField(max_length=200, blank=True, default="")


    added_on = models.DateTimeField('date added')

    def __unicode__(self):

        return '%s' % (self.title)
        return '%s' % (self.image_url)
