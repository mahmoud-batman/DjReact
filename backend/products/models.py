from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.contrib.auth import get_user_model

import uuid

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('C', 'Children')
)


def content_file_name(instance, filename):
    return '/'.join(['Items', instance.get_gender_display(),
                     instance.get_category_display(),
                     filename])


class Item(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(1)])
    discount_price = models.FloatField(
        blank=True, null=True, validators=[MinValueValidator(1)])  # discount less than price
    category = models.CharField(choices=CATEGORY_CHOICES,
                                max_length=2)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=1)
    label = models.CharField(choices=LABEL_CHOICES,
                             max_length=1)
    slug = models.SlugField(unique=True, default='',
                            editable=False, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to=content_file_name)
    rate = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while Item.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Item, self).save(*args, **kwargs)


class OrderItem(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"order of {self.user.email}"


<<<<<<< HEAD
"""
http://www.johanneshoppe.com/django-stdimage/

pip install django-stdimage
# or
pipenv install django-stdimage

from stdimage import StdImageField, JPEGField


class MyModel(models.Model):
    # works just like django's ImageField
    image = StdImageField(upload_to='path/to/img')

    # creates a thumbnail resized to maximum size to fit a 100x75 area
    image = StdImageField(upload_to='path/to/img',
                          variations={'thumbnail': {'width': 100, 'height': 75}})

    # is the same as dictionary-style call
    image = StdImageField(upload_to='path/to/img', variations={'thumbnail': (100, 75)})

    # variations are converted to JPEGs
    jpeg = JPEGField(
        upload_to='path/to/img',
        variations={'full': (None, None), 'thumbnail': (100, 75)},
    )

    # creates a thumbnail resized to 100x100 croping if necessary
    image = StdImageField(upload_to='path/to/img', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True}
    })

    ## Full ammo here. Please note all the definitions below are equal
    image = StdImageField(upload_to='path/to/img', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    }, delete_orphans=True)

For using generated variations in templates use myimagefield.variation_name.


"""
=======
>>>>>>> 4a14c5fddf637219aadb8654da3243a98b56f03b
