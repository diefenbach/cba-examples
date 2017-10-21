from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class Root(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="container",
                initial_components=[
                    components.DnDSelect(
                        selectable=["Hurz"],
                        handler={"drop": "server:handle_drop"},
                    ),
                ]
            )
        ]

    def handle_drop(self):
        import pdb; pdb.set_trace()


class View(CBAView):
    root = Root
