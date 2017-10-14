from __future__ import print_function, unicode_literals

from django.core.urlresolvers import reverse

from cba import components
from cba.base import CBAView


class LinksRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container mt",
                tag="div",
                initial_components=[
                    components.HTML(tag="h1", content="Links", css_class="mb"),
                    components.HTML(tag="p", content="A normal, a disabled and hidden link.", css_class="mb"),
                    components.Link(text="Link 1", href="."),
                    components.Link(text="Link 2", href=".", disabled=True),
                    components.Link(text="Link 3", href=".", displayed=False),
                ]
            )
        ]


class LinksView(CBAView):
    root = LinksRoot
