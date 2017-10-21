from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class Root(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="container",
                initial_components=[
                    components.HTML(tag="h1", content="History", css_class="mb mt"),
                    components.Button(
                        id="button-1",
                        value="Create new state",
                        create_state=True,
                        handler={"click": "server:handle_button|history"},
                    ),
                    components.Button(
                        id="button-2",
                        value="Create no new state",
                        create_state=False,
                        handler={"click": "server:handle_button"},
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                ]
            )
        ]

    def handle_button(self):
        result = self.get_component("result")
        result.add_component(components.HTML(content="Hurz!"))
        result.refresh()


class View(CBAView):
    root = Root
