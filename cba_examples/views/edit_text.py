from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class Root(components.Group):
    def init_components(self):

        self.html = components.HTML(
            id="html",
            content="Click to edit me!",
            css_class="mb mt",
            attributes={"style": "cursor:pointer"},
            handler={"click": "server:handle_edit"}
        )

        self.text_input = components.TextInput(
            id="text_input",
            handler={"keyup": "server:handle_save:[13,27]"},
        )

        self.initial_components = [
            components.Group(
                css_class="container",
                initial_components=[
                    components.HTML(
                        tag="h1",
                        content="Edit Text",
                        css_class="mb mt"
                    ),
                    self.html,
                ]
            )
        ]

    def handle_edit(self):
        self.text_input.value = self.html.content
        self.text_input.select_text = True
        self.replace_component("html", self.text_input)
        self.refresh()

    def handle_save(self):
        if self.key_code == "13":
            self.html.content = self.text_input.value

        self.replace_component("text_input", self.html)
        self.refresh()


class View(CBAView):
    root = Root
