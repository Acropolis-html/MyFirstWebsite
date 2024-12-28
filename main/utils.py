from django.db.models import Count
from django.core.cache import cache
from .models import Category


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = cache.get('categories')
        if not categories:
            categories = Category.objects.annotate(Count('posts'))
            cache.set('categories', categories, 60)

        menu = ''
        context['categories'] = categories
        context['menu'] = menu
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context