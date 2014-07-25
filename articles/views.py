from django.shortcuts import render

from articles.models import Category, Article

def home(request):
	trash_metal_article = Article.objects.filter(category__slug='trash-metal').order_by('-published_date')[:]
	grind_core_article = Article.objects.filter(category__slug='grind-core').order_by('-published_date')[:]
	death_metal_article = Article.objects.filter(category__slug='death-metal').order_by('-published_date')[:]


	return render(request, "home.html", {
		'death_metal_article': death_metal_article,
		'grind_core_article': grind_core_article,
		'trash_metal_article': trash_metal_article,
		})
# Create your views here.
