from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:foo>',views.category,name='category'),
    path('product/',views.product_list, name='product'),
    path('product_admin/',views.product_admin, name='product_admin'),
    path('add_product/',views.add_product, name='addproduct'),
    path('admin_sportiva/',views.admin, name='admin_sportiva'),
    path('update/<int:product_id>',views.edit_product, name='update'),
    path('delete/<int:product_id>',views.delete,name="delete")
    
]
