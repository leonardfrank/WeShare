from django import template
from space.models import Category

register = template.Library()


@register.inclusion_tag('sidebar.html')
def get_category_list(category=None):
    return {'categories': Category.objects.all(), 'current_category': category}