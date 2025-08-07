from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from .models import *
from .forms import *


def human_page(request, category_id=None, slug=None):
    categories = HumanCategory.objects.filter(is_sub_category=False)
    
    if category_id and slug:
        category = get_object_or_404(HumanCategory, id=category_id, slug=slug)
        articles = HumanArticle.objects.filter(category=category).order_by('-date_created')
    else:
        articles = HumanArticle.objects.order_by('-date_created')
    
    if not articles.exists():
        raise Http404
    
    paginator = Paginator(articles, 8)
    page_number = request.GET.get('page')
    articles_object = paginator.get_page(page_number)
    
    context = {'articles': articles_object, 'categories': categories}
    return render(request, 'human/human.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(HumanArticle, id=article_id)
    comments = HumanComment.objects.filter(article_id=article_id).order_by('-date_created')
    
    context = {
        'user': request.user,
        'article': article,
        'comments': comments
    }
    return render(request, 'human/detail.html', context)


def article_comments(request, article_id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            HumanComment.objects.create(user=request.user, article_id=article_id, comment=data['comment'])
            messages.success(request, 'نظر شما با موفقیت ثبت گردید')
            return redirect(url)
        else:
            messages.error(request, 'خطایی در ارسال نظر رخ داده است')
    else:
        return redirect(url)