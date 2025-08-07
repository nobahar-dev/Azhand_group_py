from django.shortcuts import render
from avicenna.models import AvicennaArticle
from arasto.models import ArastoArticles
from human.models import HumanArticle
from office.models import OfficeArticle
from informatics.models import InformaticsArticle
from safety.models import SafetyArticles


def home_page(request):
    avicenna_articles = AvicennaArticle.objects.all().order_by('-date_created')[:3]
    arasto_articles = ArastoArticles.objects.all().order_by('-date_created')[:3]
    human_articles = HumanArticle.objects.all().order_by('-date_created')[:3]
    office_articles = OfficeArticle.objects.all().order_by('-date_created')[:3]
    informatics_articles = InformaticsArticle.objects.all().order_by('-date_created')[:3]
    safety_articles = SafetyArticles.objects.all().order_by('-date_created')[:3]
    
    context = {
        'avicenna_articles': avicenna_articles,
        'arasto_articles': arasto_articles,
        'human_articles': human_articles,
        'office_articles': office_articles,
        'informatics_articles': informatics_articles,
        'safety_articles': safety_articles
    }
    return render(request, 'home/home.html', context)