from django.contrib import admin

from articles.models import Article, Category


class ArticleAdmin(admin.StackedInline):
	model = Article
	extra = 0

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title", {"fields": ["title"]}),
		("Slug", {"fields": ["slug"]}),
		]
	list_display = ("title",)
	list_filter = [("title"),]
	inlines = [ArticleAdmin]




admin.site.register(Category, CategoryAdmin)
# Register your models here.
