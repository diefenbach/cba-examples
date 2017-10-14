from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class RadioCheckboxRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="container",
                initial_components=[
                    components.HTML(tag="h1", content="Radio Box Group", css_class="mb mt"),
                    components.RadioCheckboxGroup(
                        id="fruits",
                        label="Fruits",
                        initial_components=[
                            components.RadioCheckbox(label="Apple", value="Apple", checked=True),
                            components.RadioCheckbox(label="Pear", value="Pear"),
                            components.RadioCheckbox(label="Orange", value="Orange"),
                            components.RadioCheckbox(label="Lemon", value="Lemon"),
                        ]
                    ),
                    components.HTML(id="result", tag="div", css_class="mb mt", content="Please select on fruit!"),
                    components.Button(id="button", value="OK", handler={"click": "server:handle_button"}),
                ]
            )
        ]

    def handle_button(self):
        fruits = self.get_component("fruits")
        result = self.get_component("result")

        result.content = "You selected: {}".format(fruits.value)
        result.refresh()


class RadioCheckboxView(CBAView):
    root = RadioCheckboxRoot
