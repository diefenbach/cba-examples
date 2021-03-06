from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class TextAreaRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="Text Input", css_class="mb mt"),
                    components.HTML(tag="p", content="Enter a text and click the button.", css_class="mbm"),
                    components.Textarea(
                        id="text",
                        label="Text",
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                    components.Button(id="button", value="OK", handler={"click": "server:handle_button"}),
                ]
            ),
        ]

    def handle_button(self):
        text = self.get_component("text")
        result = self.get_component("result")
        result.content = "You entered: {}".format(text.value)
        result.refresh()


class TextAreaView(CBAView):
    root = TextAreaRoot
