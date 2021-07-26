from django import forms
from django.forms import Textarea

from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.input_type == 'checkbox':
                field.widget.attrs['class'] = 'form-check-input'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'is_deleted')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if not isinstance(field.widget, Textarea) and field.widget.input_type == 'checkbox':
                field.widget.attrs['class'] = 'form-check-input'


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = ProductCategory.objects.filter(is_deleted=False)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if not isinstance(field.widget, Textarea) and field.widget.input_type == 'checkbox':
                field.widget.attrs['class'] = 'form-check-input'
            if field_name == 'category':
                field.widget.attrs['type'] = 'hidden'
