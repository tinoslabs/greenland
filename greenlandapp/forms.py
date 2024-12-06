from django import forms
from .models import Products,ShadeCard,Contact,PdfModel,ClientReview,GalleryModel,UvModel
class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        
class ShadeCardForm(forms.ModelForm):
    class Meta:
        model = ShadeCard
        fields = '__all__'
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class pfdForm(forms.ModelForm):
    class Meta:
        model = PdfModel
        fields = ['pdf_file']
        
class uvForm(forms.ModelForm):
    class Meta:
        model = UvModel
        fields = ['pdf_file']
        

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryModel
        fields = '__all__'