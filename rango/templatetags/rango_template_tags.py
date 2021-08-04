from django import template
from rango.models import Category,Page

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
        'current_category': current_category}

@register.inclusion_tag('rango/pages.html')
def get_page_list(current_category=None,current_page=None):
    return {'current_category': current_category,
            'pages': Page.objects.filter(category=current_category),
            'current_page': current_page,
            }
