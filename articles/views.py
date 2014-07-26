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


def category(request, category_slug):
	articles = Article.objects.filter(category__slug=category_slug).order_by('-published_date')
	category = Category.objects.get(slug=category_slug)

	return render(request, 'category.html', {
		'articles': articles,
		'category': category,
	})

def article(request, category_slug, article_id):
	article = Article.objects.get(id=article_id)

	return render(request, 'article.html', {
		'article': article,
	})


def index(request):
	articles = Article.objects.order_by('-published_date')[:3]
	category = Category.objects
	return render(request, 'index.html', {
		'articles': articles,
		'category': category,
	})
# Create your views here.
