from django import template
from ..models import MenuItems
from django.db.models import Q
from django.urls import resolve


register = template.Library()


@register.inclusion_tag('main/menu_item.html')
def draw_menu_item(item, active, children=None):
    current_children = children.get(item.id)
    return {'item': item, 'children': children, 'active': active, 'current_children': current_children}


@register.inclusion_tag('main/menu.html')
def draw_menu(menu_name, request):
    path = request.path
    url_name = resolve(path).url_name
    active = MenuItems.objects.filter(Q(menu_name=menu_name), Q(url=path) | Q(url=url_name)).first()
    items = MenuItems.objects.filter(Q(menu_name=menu_name), Q(url=path) | Q(parent_id=active.id) | Q(level__lte=active.level))

    children = {}

    for i in items:
        if children.get(i.parent_id):
            children[i.parent_id].append(i)
        else:
            children[i.parent_id] = [i]
    root = children.get(None)[0]
    return {'children': children, 'active': active, 'root': root}

