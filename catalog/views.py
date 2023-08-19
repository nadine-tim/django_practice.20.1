from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version

class GetContextMixin:
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        version_list = Version.objects.all()
        context_data['formset'] = version_list
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=0)
        context_data['formset'] = version_formset(instance=self.object)
        return context_data


class ProductCreateView(GetContextMixin, CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'image', 'category', 'price',)
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(GetContextMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
        # а также передается информация, которую заполнил пользователь
        print(f'{name} {phone} {text}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def view_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product,
        'title': 'Страница продукта',
    }
    return render(request, 'catalog/product_detail.html', context)


def home_page(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/product_list.html', context)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'catalog/home.html'
#
#
# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'objects_list': products_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/home.html', context)
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"{name}, {phone}: {message}")
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/product_detail.html'
#
#
# def view_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product,
#         'title': 'Страница продукта',
#     }
#     return render(request, 'catalog/product_detail.html', context)
