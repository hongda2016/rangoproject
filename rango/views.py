from django.shortcuts import render
from .models import Category
from .models import Page
# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories':category_list}
    return render(request,'rango/index.html',context_dict)


def category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['page'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request,'rango/category.html',context_dict)
