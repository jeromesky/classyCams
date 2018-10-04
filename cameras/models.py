from django.db import models
from cameras.helper import RenameUploadedFileName
from django.contrib.auth.models import User
from django.forms import forms





# Create your models here.
class Company(models.Model):
    name       = models.CharField(max_length=50)
    bios       = models.TextField(null=False, blank=True)
    insertDate = models.DateField('Date Created',auto_now_add='true')
    url        = models.URLField(max_length=100, null=False, blank=True)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Brand(models.Model):
    name       = models.CharField(max_length=20)
    insertDate = models.DateField('Date Created', auto_now_add='true')
    company    = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        # ' ( ' + Company().getName() + ' )'#
        # return self.name

class Type(models.Model):
    label       = models.CharField(max_length=45)
    description = models.CharField(max_length=300)
    group       = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.label



class Collection(models.Model):
    user        = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    name        = models.CharField(max_length=80)
    bios        = models.TextField(blank=True)
    contact     = models.CharField(max_length=50,  help_text='Contact Name for this Collection, *information is Public')
    number      = models.CharField('Phone Number', help_text='Conact Number *not public',  max_length=18, null=True, blank=True)
    email       = models.EmailField('Email Address ', help_text='*only public if you wish, by selecting checkbox bellow.', max_length=40, null=True, blank=True)
    emailpublic = models.BooleanField('Make my Email Address visible', help_text='Selecting this option will display your Email Address on the public web pages.', default=0)
    # country     = models.ForeignKey(country)
    city        = models.CharField(max_length=35)
    url         = models.URLField(max_length=100,  help_text='If you have a webpage you would like guest to viste, please supply here.',  null=True, blank=True)
    insertDate = models.DateTimeField('Date Created', auto_now_add='true')
    updateDate = models.DateTimeField('Date Updated', auto_now=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    name         = models.CharField(max_length=60)
    modelNumber  = models.CharField('Model Number', max_length=20)
    brand        = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type         = models.ForeignKey(Type, on_delete=models.CASCADE)
    releasedDate = models.DateField('Product Release Date', blank=True, null=True)
    photo        = models.FileField(upload_to=RenameUploadedFileName('cameras'), max_length=30)
    insertDate   = models.DateTimeField('Date Created',auto_now_add='true')
    updateDate   = models.DateTimeField('Date Updated', auto_now=True)
    collection   = models.ForeignKey(Collection, on_delete=models.CASCADE)
    # photo        = models.FileField(upload_to='products/%Y/%m/%d/', max_length=40)#'product'
    # photo        = models.FileField(upload_to=path_and_rename("complaint_files", 'pro_'), max_length=500, help_text="Browse a file")

    list_filter = ('name',)

    def __str__(self):
        return self.name