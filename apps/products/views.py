from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from .models import Category, Product


def home(requests):
    context = {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'publications': Publication.objects.all().order_by('-created')[:5]
    }

    return render(request=requests, template_name='index.html')


class Index(ListView):
    model = Product
    extra_context = {'title': 'Главная страница'}
    template_name = 'products/index.html'
    context_object_name = "products"

    def get_queryset(self):
        """Вывод родительской категорий"""
        # categories = Category.objects.filter(parent=None)
        products = Product.objects.all()
        return products


class SubCategories(ListView):
    """
    Вывод подкатегории на отдельной страничке
    """
    model = Product
    context_object_name = 'products'
    template_name = 'products/category_page.html'

    def get_queryset(self):
        """
        Получение всех товаров подкатегории
        """
        parent_category = Category.objrcts.get(slug=self.kwargs['slug'])
        subcategories = parent_category.subcategories.all()
        products = Product.objects.fillter(category__in=subcategories).order_by('?')
        return products


class ProductPage(DetailView):
    """
    вывод товара на отд.страницу
    """
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_page.html'


