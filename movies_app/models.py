from django.db import models
from django.utils.text import slugify


class Movie(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=40)
    directors = models.ManyToManyField('Director')
    studio = models.ForeignKey('Studio', on_delete=models.CASCADE)
    released_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='cover_image')
    genre = models.ManyToManyField('Genre')
    asin = models.CharField('ASIN', max_length=10)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Movie, self).save(*args, **kwargs)

    def amazon_url(self):
        return "https://www.amazon.com/dp/" + self.asin

    def __str__(self):
        return self.title


class Director(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512, blank=True)
    middle_name = models.CharField(max_length=512, blank=True)
    phone_number = models.DecimalField(max_digits=10, decimal_places=0)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name


class Studio(models.Model):
    title = models.CharField(max_length=512)
    prefix = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Studio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    review = models.CharField(max_length=2000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.review