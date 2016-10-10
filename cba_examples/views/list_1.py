from __future__ import print_function, unicode_literals

from cba import components
from cba.views import CBAView


class LinksRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container mt",
                initial_components=[
                    components.HTML(tag="h1", content="An unordered list", css_class="mb"),
                    components.List(
                        css_class="mb",
                        type="ul",
                        initial_components=[
                            components.HTML(tag="div", content="One"),
                            components.HTML(tag="div", content="Two"),
                            components.HTML(tag="div", content="Three"),
                        ],
                    ),
                    components.HTML(tag="h1", content="An ordered list", css_class="mb"),
                    components.List(
                        css_class="mb",
                        type="ol",
                        initial_components=[
                            components.HTML(tag="div", content="One"),
                            components.HTML(tag="div", content="Two"),
                            components.HTML(tag="div", content="Three"),
                        ],
                    ),
                ]
            )
        ]


class LinksView(CBAView):
    root = LinksRoot
