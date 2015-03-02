from django.db import models

# Create your models here.

from django.contrib import admin

class SimpleReadWrite(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)


    def __str__(self):
        return self.name

admin.site.register(SimpleReadWrite)


class ImageStore(models.Model):
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url

admin.site.register(ImageStore)



class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    image = models.ForeignKey(ImageStore, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)


    def __str__(self):
        return self.name

admin.site.register(Item)



class FieldSample(models.Model):
    required_field = models.IntegerField()
    required_field_with_default = models.IntegerField(default=1)
    nullable_field = models.IntegerField(null=True, blank=True)
    nullable_field_with_default = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return self.pk

admin.site.register(FieldSample)



