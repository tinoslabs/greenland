"""
URL configuration for greenlandpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from ckeditor_uploader import views as ckeditor_views
urlpatterns = [
    path('', views.index, name='index'),
    
    
    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    
    path('add_client_reviews',views.add_client_reviews,name='add_client_reviews'),
    path('view_client_reviews',views.view_client_reviews,name='view_client_reviews'),
    path('update_client_reviews/<int:id>/',views.update_client_reviews,name='update_client_reviews'),
    path('delete_client_review/<int:id>/',views.delete_client_review,name='delete_client_review'),
    
    path('add_product',views.add_product,name='add_product'),
    path('view_product',views.view_product,name='view_product'),
    path('update_product/<int:id>/',views.update_product,name='update_product'),
    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
    
    path('add_shade_card',views.add_shade_card,name='add_shade_card'),
    path('view_card',views.view_card,name='view_card'),
    path('update_card/<int:id>/',views.update_card,name='update_card'),
    path('delete_card/<int:id>/',views.delete_card,name='delete_card'),
    

    path('products', views.products, name='products'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('shade_card', views.shade_card, name='shade_card'),

    path('view_contact', views.view_contact, name='view_contact'),
    path('delete_contact/<int:id>/',views.delete_contact, name='delete_contact'),
    
    path('upload_brochure', views.upload_brochure, name='upload_brochure'),
    path('view_brochures', views.view_brochures, name='view_brochures'),
    path('update/<int:pk>/', views.update_brochure, name='update_brochure'),
    path('delete/<int:pk>/', views.delete_brochure, name='delete_brochure'),
       
    path('add_gallery', views.add_gallery, name='add_gallery'),
    path('gallery_view', views.gallery_view, name='gallery_view'),
    path('update_gallery/<int:id>/', views.update_gallery, name='update_gallery'),
    path('delete_gallery/<int:id>/', views.delete_gallery, name='delete_gallery'),
       
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('gallery', views.gallery, name='gallery'),
    
    path('uv_brochure', views.uv_brochure, name='uv_brochure'),
    path('view_uv_brochures', views.view_uv_brochures, name='view_uv_brochures'),
    path('update_uv_brochure/<int:pk>', views.update_uv_brochure, name='update_uv_brochure'),
    path('delete_uv_brochure/<int:pk>', views.delete_uv_brochure, name='delete_uv_brochure'),

]
