from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
    

# UNI-ISOL models
class Work(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    cover_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.ForeignKey(Work, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

# end UNI-ISOL models