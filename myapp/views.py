import logging

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ProductForm
from .models import Product


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'myapp/index.html')


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}')

    else:
        form = UserForm()
    return render(request, 'myapp/user_form.html', {'form': form})

def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp/many_fields_form.html', {'form': form})


def add_product_info(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            how_many = form.cleaned_data['how_many']
            date_create = form.cleaned_data['date_create']
            photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)

            product = Product(name=name,
                              price=price,
                              description=description,
                              how_many=how_many,
                              date_create=date_create,
                              photo=photo.name)
            product.save()
            message = 'Данные по товару успешно сохранены'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'myapp/product_form.html', {'form': form, 'message': message})
