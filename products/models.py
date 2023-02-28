from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# 3d party imports
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, editable=False, help_text='Unique name for product page URL')
    description = models.TextField(help_text='brief description of the product')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='price for the product')
    quantity = models.IntegerField(help_text='quantity of the product in stock')
    image = models.ImageField(upload_to='products/images/', help_text='main image of the product')
    resized_image = ImageSpecField(source='image',
                                   processors=[ResizeToFit(500, 500)],
                                   format='JPEG',
                                   options={'quality': 99})

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def generate_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            print(unique_slug)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        return super().save(*args, **kwargs)


@receiver(pre_save, sender=Product)
def set_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.generate_unique_slug()


product = Product.objects.all()[0]
print(product.resized_image.url)
print(product.resized_image.width)
