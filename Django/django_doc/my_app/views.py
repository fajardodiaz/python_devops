from django.shortcuts import render
from .models import Article, Reporter

# Create your views here.

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year = year)
    context = {'year':year, 'article_list':a_list}
    return render(request,'/home/pablo/Documentation/Python/Django/django_doc/my_app/templates/year_archive.html',context)

def month_archive():
    return "Month"

def article_detail():
    return "Article"