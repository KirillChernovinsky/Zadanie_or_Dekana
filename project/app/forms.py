from django import forms


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=40)
    product_categori = forms.CharField(max_length=40)
    product_description = forms.CharField(max_length=400)
    product_img = forms.URLField()


