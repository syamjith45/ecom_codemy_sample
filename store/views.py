from django.shortcuts import render,redirect
from .models import Category, Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import get_object_or_404
# Create your views here.
def category(request,foo):
    try:
        category=Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products, 'category':category})
    except:
        messages.success(request,("category doesn't exist........"))
        return redirect('home')
def product(request,pk):
    products = Product.objects.get(id=pk)
    return render(request,'product.html',{'products': products})
def product_admin(request):
    products = Product.objects.all()
    return render(request,'product1.html',{'product': products})
def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products': products})

def about(request):
    
    return render(request,'about.html')

def admin(request):
    
    return render(request,'admin.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            if request.user.is_superuser:
                # If the logged-in user is an admin, redirect to the admin home page
                return redirect('admin_sportiva')  # Replace with your actual admin home URL name
            else:
                messages.success(request, 'You have been logged in.')
                return redirect('home')  # Redirect to the home page for regular users
        else:
            messages.error(request, 'Invalid credentials. Please check the username and password.')
            return redirect('login')  # Redirect back to the login page

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("you have beeen logged out ..."))
    return redirect('home')
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,("you have Registered ..."))
            return redirect('home')
        else:
            messages.success(request,("Whoops...... There was problem in registering"))
            return redirect('register')
    else:     
        return render(request,'register.html',{'form':form})
    
# def add_product(request):
#     if request.method == 'POST':
#         # Retrieve form data from the request
#         p_name = request.POST.get('productName')
#         category = request.POST.get('category')
#         price = request.POST.get('productPrice')
# The view store.views.delete didn't return an HttpResponse object. It returned None instead.        stock = request.POST.get('productStock')
#         image = request.POST.get('productImage')
        
#         product = Product.objects.create(
#             name=p_name,
#             category_id=category,
#             price=price,
#             stock=stock,
#             image=image
#         )
#         return redirect('product')
#     categories = Category.objects.all()
#     return render(request, 'addproduct.html',{'category': categories})

def product_list(request):
    products=Product.objects.all()
    return render(request,'product1.html',{'products':products})


def my_view(request):
    categories = Category.objects.all()
    return render(request, 'addproduct.html', {'category': categories})

from .forms import ProductForm  # You need to create a form to handle the input data

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product')  # Redirect to the product list page after successful form submission
#     else:
#         form = ProductForm()

#     categories = Category.objects.all()
#     return render(request, 'addproduct.html', {'form': form, 'categories': categories})
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')  # Update the redirect to the correct URL name
    else:
        form = ProductForm()

    categories = Category.objects.all()
    return render(request, 'addproduct.html', {'form': form, 'categories': categories})


def edit_product(request, product_id):
    # Get the product instance based on the product_id
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')  # Redirect to the product list page after successful form submission
    else:
        form = ProductForm(instance=product)

    categories = Category.objects.all()
    return render(request, 'update.html', {'form': form, 'categories': categories})

from django.shortcuts import render, get_object_or_404, redirect


# def delete_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == 'POST':
#         product.delete()
#         # Optionally, you can add a success message
#         return redirect('product')  # Change 'product_list' to your product list URL name

#     return render(request, 'delete.html', {'product': product})
def delete(request, product_id):
    if request.method == "POST":
        Product.objects.get(id=product_id).delete()
        return redirect('product')