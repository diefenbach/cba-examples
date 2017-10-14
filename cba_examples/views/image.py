from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class ImageRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="Image", css_class="mb mt"),
                    components.HTML(tag="p", content="Move the mouse over the image.", css_class="mbm"),
                    components.Image(
                        id="image",
                        src="https://www.python.org/static/img/python-logo.png",
                        handler={
                            "mouseover": "server:handle_mouse_over",
                            "mouseout": "server:handle_mouse_out",
                        },
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                ],
            ),
        ]

    def handle_mouse_over(self):
        result = self.get_component("result")
        result.content = "Mouse over!"
        result.refresh()

    def handle_mouse_out(self):
        result = self.get_component("result")
        result.content = "Mouse out!"
        result.refresh()


class ImageView(CBAView):
    root = ImageRoot
