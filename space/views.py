# coding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Category, Page
from .forms import CategoryForm, PageForm
# Create your views here.


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    all_category = Category.objects.all()
    context_dict = {'categories': category_list, 'pages': page_list,
                    'all_categories': all_category}
    return render(request, 'space/index.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        cat_specifiy = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = cat_specifiy.name
        pages = Page.objects.filter(category=cat_specifiy).order_by('-views')
        context_dict['pages'] = pages
        context_dict['category'] = cat_specifiy
    except Category.DoesNotExist:
        return render(request, '404.html')
    return render(request, 'space/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render(request, 'space/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        return render(request, '404.html')
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=True)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    return render(request, 'space/add_page.html', {'form': form, 'category': cat})


def track_url(request):
    url = '/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views += 1
                page.save()
                url = page.url
            except Page.DoesNotExist:
                return render(request, '404.html')

    return redirect(url)


@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['cat_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()
    return HttpResponse(likes)


def about_us(request):
    return render(request, 'space/about_us.html')
