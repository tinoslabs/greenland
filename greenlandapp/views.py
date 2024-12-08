from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import ClientReview,Products,ShadeCard,Contact,PdfModel,GalleryModel,UvModel
from .forms import ClientReviewForm,ProductForm,ShadeCardForm,ContactForm,pfdForm,GalleryForm,uvForm

# Create your views here.

def index(request):
    client_reviews = ClientReview.objects.all()
    brochure = PdfModel.objects.all()
    gallery = GalleryModel.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'client_reviews': client_reviews, 'form': form,'brochure':brochure,'gallery':gallery})


@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.success(request, ("There Was An Error Loging In, Try Again..."))
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')

 
@login_required(login_url='user_login')
def admin_dashboard(request):
    return render(request,'admin_pages/admin_dashboard.html')

@login_required(login_url='user_login')
def add_client_reviews(request):
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews') 
    else:
        form = ClientReviewForm()

    return render(request, 'admin_pages/add_client_reviews.html', {'form': form})


@login_required(login_url='user_login')
def view_client_reviews(request):
    client_reviews = ClientReview.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_client_reviews.html', {'client_reviews': client_reviews})


@login_required(login_url='user_login')
def update_client_reviews(request, id):
    client_reviews = get_object_or_404(ClientReview, id=id)
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews')
    else:
        form = ClientReviewForm(instance=client_reviews)
    return render(request, 'admin_pages/update_client_reviews.html', {'form': form, 'client_reviews': client_reviews})
    

@login_required(login_url='user_login')
def delete_client_review(request,id):
    client_reviews = ClientReview.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_client_reviews')


@login_required(login_url='user_login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_product') 
    else:
        form = ProductForm()

    return render(request, 'admin_pages/add_product.html', {'form': form})


@login_required(login_url='user_login')
def view_product(request):
    product = Products.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_product.html', {'product': product})


@login_required(login_url='user_login')
def update_product(request, id):
    product = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin_pages/update_product.html', {'form': form, 'product': product})
    

@login_required(login_url='user_login')
def delete_product(request,id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('view_product')

@login_required(login_url='user_login')
def add_shade_card(request):
    if request.method == 'POST':
        form = ShadeCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_card') 
    else:
        form = ProductForm()

    return render(request, 'admin_pages/add_shade_card.html', {'form': form})


@login_required(login_url='user_login')
def view_card(request):
    card = ShadeCard.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_card.html', {'card': card})


@login_required(login_url='user_login')
def update_card(request, id):
    card = get_object_or_404(ShadeCard, id=id)
    if request.method == 'POST':
        form = ShadeCardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('view_card')
    else:
        form = ShadeCardForm(instance=card)
    return render(request, 'admin_pages/update_card.html', {'form': form, 'card': card})
    

@login_required(login_url='user_login')
def delete_card(request,id):
    card = ShadeCard.objects.get(id=id)
    card.delete()
    return redirect('view_card')



def about(request):
    brochure = PdfModel.objects.all()
    return render(request,'about.html',{'brochure':brochure})

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     return render(request,'contact.html',{'form':form})

def contact(request):
    brochure = PdfModel.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return render(request, 'contact.html', {'form': ContactForm()})  # Clear the form after success
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'brochure':brochure})

@login_required(login_url='user_login')
def view_contact(request):
    contact = Contact.objects.all().order_by('-id')
    return render(request,'admin_pages/view_contact.html',{'contact':contact})

@login_required(login_url='user_login')
def delete_contact(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('view_contact')


def upload_brochure(request):
    if request.method == 'POST':
        form = pfdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_brochures')
    else:
        form = pfdForm()
    return render(request, 'admin_pages/upload_brochure.html', {'form': form})

# View to display all brochures
def view_brochures(request):
    brochures = PdfModel.objects.all().order_by('-upload_date')
    return render(request, 'admin_pages/view_brochures.html', {'brochures': brochures})

# View to update a brochure
def update_brochure(request, pk):
    brochure = get_object_or_404(PdfModel, pk=pk)
    if request.method == 'POST':
        form = pfdForm(request.POST, request.FILES, instance=brochure)
        if form.is_valid():
            form.save()
            return redirect('view_brochures')
    else:
        form = pfdForm(instance=brochure)
    return render(request, 'admin_pages/update_brochure.html', {'form': form})

# View to delete a brochure
def delete_brochure(request, pk):
    brochure = get_object_or_404(PdfModel, pk=pk)
    if request.method == 'POST':
        brochure.delete()
    return redirect('view_brochures')
    


def service(request):
    brochure = PdfModel.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
    else:
        form = ContactForm()
    return render(request,'service.html',{'brochure':brochure,'form':form})


def products(request):
    products = Products.objects.all()
    brochure = PdfModel.objects.all()
    return render(request,'products.html',{'products':products,'brochure':brochure})

# def product_details(request):
#     return render(request,'product_details.html')

def product_details(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'product_details.html', {'product': product})


def shade_card(request):
    shade_cards = ShadeCard.objects.all()
    file = UvModel.objects.all()
    brochure = PdfModel.objects.all()
    return render(request,'shade_card.html',{'shade_cards':shade_cards,'brochure':brochure,'file':file})

def gallery(request):
    brochure = PdfModel.objects.all()
    return render(request,'gallery.html',{'brochure':brochure})

@login_required(login_url='user_login')
def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_view') 
    else:
        form = GalleryForm()

    return render(request, 'admin_pages/add_gallery.html', {'form': form})


@login_required(login_url='user_login')
def gallery_view(request):
    gallery = GalleryModel.objects.all().order_by('-id')
    return render(request,'admin_pages/gallery_view.html',{'gallery':gallery})


@login_required(login_url='user_login')
def update_gallery(request, id):
    gallery = get_object_or_404(GalleryModel, id=id)

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('gallery_view')
    else:
        form = GalleryForm(instance=gallery)

    return render(request, 'admin_pages/update_gallery.html', {'form': form,'gallery':gallery})


@login_required(login_url='user_login')
def delete_gallery(request,id):
    gallery = GalleryModel.objects.get(id=id)
    gallery.delete()
    return redirect('gallery_view')



def shade_card_brochure(request):
    if request.method == 'POST':
        form = uvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_card_brochure')
    else:
        form = uvForm()
    return render(request, 'admin_pages/shade_card_brochure.html', {'form': form})

# View to display all brochures
def view_card_brochure(request):
    brochures = UvModel.objects.all().order_by('-upload_date')
    return render(request, 'admin_pages/view_card_brochure.html', {'brochures': brochures})

# View to update a brochure
def update_card_brochure(request, pk):
    brochure = get_object_or_404(UvModel, pk=pk)
    if request.method == 'POST':
        form = uvForm(request.POST, request.FILES, instance=brochure)
        if form.is_valid():
            form.save()
            return redirect('view_card_brochure')
    else:
        form = uvForm(instance=brochure)
    return render(request, 'admin_pages/update_card_brochure.html', {'form': form})

# View to delete a brochure
def delete_card_brochure(request, pk):
    brochure = get_object_or_404(UvModel, pk=pk)
    if request.method == 'POST':
        brochure.delete()
    return redirect('view_card_brochure')


from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.http import JsonResponse

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})