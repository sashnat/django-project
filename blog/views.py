from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Точка перед models означает текущую директорию или текущее приложение
# Поскольку views.py и models.py находятся в одной директории,
# мы можем использовать точку . и имя файла (без расширения .py).
# Затем мы импортируем модель (Post).
def post_list(request):
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# мы создали переменную для QuerySet: posts
    return render(request, 'blog/post_list.html', {'posts': posts})
