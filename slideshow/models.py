from django.db import models
from django.contrib import admin


# Create your models here.

class SlideImage(models.Model):
    src = models.FileField(upload_to='images/')
    width = models.IntegerField()
    height =  models.IntegerField()
    title = models.CharField(max_length=150)
    alt = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class SlideImageAdmin(admin.ModelAdmin):

    list_display = ('title', 'alt', 'width', 'height')

admin.site.register(SlideImage, SlideImageAdmin)