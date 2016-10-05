from __future__ import print_function, unicode_literals

from cba import components
from cba.views import CBAView


class TextInputRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="Text Input", css_class="mb mt"),
                    components.TextInput(
                        id="name-1",
                        label="Name",
                        placeholder="Please enter your name!",
                        icon="user",
                    ),
                    components.HTML(id="result-1", tag="div", css_class="mt mb"),
                    components.Button(id="button-1", value="OK", handler={"click": "server:handle_button"}),
                ]
            ),
        ]

    def handle_button(self):
        name = self.get_component("name-1")

        if name.value == "":
            name.error = "Your name is required!"
        else:
            name.error = ""
            result = self.get_component("result-1")
            result.content = "You entered: {}".format(name.value)
            result.refresh()

        name.refresh()


class TextInputView(CBAView):
    root = TextInputRoot
