from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
import datetime as dt


# def index(request):
# # одна строка вместо тысячи слов на SQL
#     latest = Post.objects.order_by('-pub_date')[:10]
#     # собираем тексты постов в один, разделяя новой строкой
#     output = []
#     for item in latest:
#         output.append(item.text)
#     return HttpResponse('\n'.join(output))

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

# Совсем неправильно, функция вернет None: забыли return
def index_wrong(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        render(request, "index.html", {"posts": latest})

# Хороший вариант: промежуточные переменные полезны
def index_ok(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        response = render(request, "index.html", {"posts": latest})
        return response

# Хороший вариант: без промежуточных переменных - короче
def index_ok_too(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        return render(request, "index.html", {"posts": latest})


