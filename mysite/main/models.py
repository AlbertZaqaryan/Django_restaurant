from django.db import models

# Create your models here.

class AboutUs(models.Model):

    text = models.TextField('AboutUs text')
    experience = models.PositiveIntegerField('AboutUs experience')
    chef = models.PositiveIntegerField('AboutUs chef')
    img1 = models.ImageField('AboutUs image1', upload_to='about_images')
    img2 = models.ImageField('AboutUs image2', upload_to='about_images')
    img3 = models.ImageField('AboutUs image3', upload_to='about_images')
    img4 = models.ImageField('AboutUs image4', upload_to='about_images')

    def __str__(self):
        return self.text
    

class MenuFood(models.Model):

    name = models.CharField('MenuFood name', max_length=100)
    about = models.TextField('MenuFood about')
    img = models.ImageField('MenuFood image', upload_to='menu_images')
    price = models.PositiveIntegerField('MenuFood price')

    def __str__(self):
        return self.name
    

class Book(models.Model):

    name = models.CharField('Book user name', max_length=100)
    email = models.EmailField('Book user email')
    date_time = models.CharField('Book user date time', max_length=100)
    count_people = models.PositiveIntegerField('Book people count')
    subject = models.TextField('Book subject')

    def __str__(self):
        return self.name
    

class Contact(models.Model):

    name = models.CharField('Contact user name', max_length=100)
    email = models.EmailField('Contact user email')
    subject = models.CharField('Contact subject', max_length=255)
    message = models.TextField('Contact message')

    def __str__(self):
        return self.name