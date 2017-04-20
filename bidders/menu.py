# coding: utf-8
from django.utils.safestring import mark_safe
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from categories.models import Category


class BiddersSubMenu(CMSAttachMenu):
    name = "Bidder SubMenu"

    def get_nodes(self, request):
        nodes = []

        for cat in Category.objects.all():
            node = NavigationNode(
                mark_safe(cat.name),
                cat.get_absolute_url(),
                cat.id
            )
            nodes.append(node)

        return nodes

menu_pool.register_menu(BiddersSubMenu)
