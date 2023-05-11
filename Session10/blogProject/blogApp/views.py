from django.shortcuts import render, get_object_or_404
from .models import Category, Article, Comment, Recomment
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
    comments = post.comments.all()
    if request.method == 'POST':
        content = request.POST.get('content')
        comment_id = request.POST.get('comment_id')
    
        if comment_id:
            comment = Comment.objects.get(pk=comment_id)
            Recomment.objects.create(comment = comment, content = content)
            return redirect('detail', post_pk)

        else:
            Comment.objects.create(article = post, content= content ) 
            return redirect('detail', post_pk)
        
    return render(request, 'detail.html', {'post':post, 'comments':comments})