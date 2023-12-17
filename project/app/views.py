from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import ProductForm

from .models import Product


# from .forms import AddForm, UserForm
# from .models import News, Comment, Person



def index(request):
    product = Product.objects.all()
    print(product)
    return render(request, 'main.html', context={'product': product})





def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_categori = form.cleaned_data['product_categori']
            product_description = form.cleaned_data['product_description']
            product_img = form.cleaned_data['product_img']
            men, _ = Product.objects.get_or_create(product_name=product_name,
                                                   product_categori=product_categori,
                                                   product_description=product_description,
                                                   product_img=product_img)
            return redirect('home')
        else:
            form = ProductForm()

            return render(request, 'create_product.html', context={'form': form})
    else:
        form = ProductForm()
        return render(request, 'create_product.html', context={'form': form})





def delete(request, id):
    try:
        men = Product.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        pass






# Не понял как сделать фильтр для поиска по категориям(

# def telefoni(request):
#     telefon = Product.objects.filter(product_categori='Телефоны')
#     print(telefon)
#     product_name = telefon.cleaned_data['product_name']
#     product_categori = telefon.cleaned_data['product_categori']
#     product_description = telefon.cleaned_data['product_description']
#     product_img = telefon.cleaned_data['product_img']
#     men, _ = Product.objects.get_or_create(product_name=product_name,
#                                            product_categori=product_categori,
#                                            product_description=product_description,
#                                            product_img=product_img)
#     return redirect('home')




