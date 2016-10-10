from __future__ import print_function, unicode_literals

from cba import components
from cba.views import CBAView


class CheckboxRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="container",
                initial_components=[
                    components.HTML(tag="h1", content="Checkbox Group", css_class="mb mt"),
                    components.CheckboxGroup(
                        id="fruits",
                        label="Fruits",
                        initial_components=[
                            components.Checkbox(label="Apple", value="Apple", checked=True),
                            components.Checkbox(label="Pear", value="Pear"),
                            components.Checkbox(label="Orange", value="Orange", checked=True),
                            components.Checkbox(label="Lemon", value="Lemon"),
                        ]
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb", content="Please select one ore more fruits!"),
                    components.Button(
                        id="button",
                        value="OK",
                        handler={"click": "server:handle_button"}),
                ]
            )
        ]

    def handle_button(self):
        fruits = self.get_component("fruits")
        result = self.get_component("result")

        result.content = "You selected: {}".format(fruits.value)
        result.refresh()


class CheckboxView(CBAView):
    root = CheckboxRoot
