from django.core.paginator import Paginator
from account.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from account.mixins import AuthorAccessMixin
# from django.http import Http404
from .models import Article, Category
from django.db.models import Q

# Create your views here.
class ArticleList(ListView):
  queryset = Article.objects.published()
  paginate_by = 3


class ArticleDetail(DetailView):
  def get_object(self):
    slug = self.kwargs.get("slug")
    article = get_object_or_404(Article.objects.published(), slug=slug)
    
    ip_address = self.request.user.ip_address
    viewsCount = article.hits.all()
    if ip_address not in viewsCount:
      article.hits.add(ip_address)
    
    return article
  
  
class ArticlePreview(AuthorAccessMixin, DetailView):
  def get_object(self):
    pk = self.kwargs.get("pk")
    return get_object_or_404(Article, pk=pk)
  

class CategoryList(ListView):
  paginate_by = 3
  template_name = "blog/category_list.html"
  
  def get_queryset(self):
    global category
    slug = self.kwargs.get("slug")
    category = get_object_or_404(Category.objects.active(), slug=slug)
    return category.articles.published()
  
  def get_context_data(self, **kwargs):
    slug = self.kwargs.get("slug")
    context = super().get_context_data(**kwargs)
    context["category"] = category
    return context
  
  
class AuthorList(ListView):
  paginate_by = 3
  template_name = "blog/author_list.html"
  
  def get_queryset(self):
    global author
    username = self.kwargs.get("username")
    author = get_object_or_404(User, username=username)
    return author.articles.published()
  
  def get_context_data(self, **kwargs):
    slug = self.kwargs.get("slug")
    context = super().get_context_data(**kwargs)
    context["author"] = author
    return context


class SearchList(ListView):
  paginate_by = 3
  template_name = "blog/search_list.html"
  
  def get_queryset(self):
    search = self.request.GET.get("q")
    return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["search"] = self.request.GET.get("q")
    return context