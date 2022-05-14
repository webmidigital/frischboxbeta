from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Products Model




class Packages(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactive', 'Deactive'),
    )
    id = models.AutoField
    name = models.CharField(max_length=100)
    description = HTMLField()
    Mrp = models.FloatField(max_length=100)
    sale_price = models.FloatField(max_length=100)
    quantity = models.CharField(max_length=10)
    Delivery_type = models.CharField(max_length=200)
    Delivery_Days= models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="packages/")
    paylink = models.CharField(max_length=200)


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Packages"


class Statelist(models.Model):
    id = models.AutoField
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

    class Meta:
        verbose_name_plural = "Statelist"


class our_cities(models.Model):
    id = models.AutoField
    state_name = models.ForeignKey(Statelist, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    city_area = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = "our_cities"


class Bulk_orders(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    mobile = PhoneNumberField(unique=True, null=False, blank=False)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Bulk_orders"


class General_enquiries(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    mobile = PhoneNumberField(unique=True, null=False, blank=False)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "General_enquiries"


class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = HTMLField()
    feature_image = models.ImageField(null=True, blank=True, upload_to="post/")
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Policies(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    description = HTMLField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Policies"

class sliderimages(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="slider/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "slider images"
