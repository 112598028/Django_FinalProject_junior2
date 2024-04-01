from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model): 
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save()
    
class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)


# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(default='', blank=True, upload_to='images')
    # image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(350, 200)], format='JPEG', options={'quality':60})
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower, self).save()
        
    def get_absolute_url(self): 
        return reverse('detail', args=[str(self.slug)])
