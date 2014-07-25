from django.shortcuts import render

from articles.models import Category, Article

def home(request):
	trash_metal_articles = Article.objects.filter(category__slug='trash-metal').order_by('-published_date')[:]
	grind_core_articles = Article.objects.filter(category__slug='grind-core').order_by('-published_date')[:]
	death_metal_articles = Article.objects.filter(category__slug='death-metal').order_by('-published_date')[:]


	return render(request, "home.html", {
		'death_metal_articles': death_metal_articles,
		'grind_core_articles': grind_core_articles,
		'trash_metal_articles': trash_metal_articles,
		})
# Create your views here.
