from django import forms
from .models import ClientReview,Products,ShadeCard,Contact,Brochure,BrochureModel

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
        

class BrochureForm(forms.ModelForm):
    class Meta:
        model = BrochureModel
        fields = ['pdf_file']
        
