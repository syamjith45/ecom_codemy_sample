from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
  
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['p_name', 'price', 'category', 'description', 'image', 'stock', 'is_sale', 'sale_price','slug']
        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 400px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 400px;'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-sm', 'style': 'max-width: 400px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 400px;'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-sm', 'accept': 'image/*', 'style': 'max-width: 400px;'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 400px;'}),
            'is_sale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control form-control-sm','style': 'max-width: 400px;'}),
            'slug': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'max-width: 400px;'}),
        }
        labels = {
            'p_name': 'Product Name',
            'price': 'Price',
            'category': 'Category',
            'description': 'Product Description',
            'image': 'Product Image',
            'stock': 'Stock',
            'is_sale': 'On Sale',
            'sale_price': 'Sale Price',
        }


