from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class ClientReview(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    
    review = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.review}"
    
    
class Products(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    details = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.product_name or 'Unnamed Product'
    
    
class ShadeCard(models.Model):
    card_name = models.CharField(max_length=100, null=True, blank=True)
    card_image = models.ImageField(upload_to='images/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.card_name or 'Unnamed Product'

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
      
class PdfModel(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pdf_file.name.split('/')[-1]
    
class UvModel(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pdf_file.name.split('/')[-1]
    
        
class GalleryModel(models.Model):
    gallery_image = models.ImageField(upload_to='images/')

    

    
    

    

 
 
    

    
    
