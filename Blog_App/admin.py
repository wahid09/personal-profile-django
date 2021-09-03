from django.contrib import admin
from Blog_App.models import Author, Category, Article

# Register your models here.

class authoModel(admin.ModelAdmin):
    list_display = ["__str__", "active"]
    search_fields = ["__str__", "details"]
    class Meta:
        Model = Author
admin.site.register(Author, authoModel)

class categoryModle(admin.ModelAdmin):
    list_display = ['name', 'active']
    search_fields = ["__str__"]
    class Meta:
        Model = Category
admin.site.register(Category, categoryModle)

class articleModel(admin.ModelAdmin):
    list_display = ['__str__', 'article_author', 'category', 'articate_image', 'publish_date', 'update_date', 'active']
    search_fields = ['__str__', 'title', 'body', 'category']
    list_filter = ['category', 'article_author', 'publish_date']
    list_per_page = 15
    list_max_show_all = 50
    class Meta:
        Model: Article
admin.site.register(Article, articleModel)
