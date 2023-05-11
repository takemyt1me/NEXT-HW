from django.shortcuts import render
from .models import Category, Article
from django.shortcuts import redirect
# Create your views here.

def home(request):
    categories = Category.objects.all()

    return render(request, 'home.html', {'categories': categories})

def new(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')

        category = Category.objects.get(id=category_id)
        article = Article.objects.create(title=title, content=content, category=category)
        return redirect('detail', article.pk)
    else:
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'new.html', context)
    
def category(request, category_pk):
    category_post = Article.objects.filter(category=category_pk)

    return render(request, 'category.html', {'category_post': category_post})

def detail(request, post_pk):
    post = Article.objects.get(pk=post_pk)
    created_at = post.created_at

    return render(request, 'detail.html', {'post':post, 'created_at':created_at})