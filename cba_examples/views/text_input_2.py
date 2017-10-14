from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class TextInputRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="Text Input with local Javascript", css_class="mb mt"),
                    components.TextInput(
                        id="name-2",
                        label="Name",
                        placeholder="Please enter your name!",
                        icon="user",
                        handler={"keyup": "client:MyCopyTo"},
                        javascript="function MyCopyTo() { $('#result-2').html($('#name-2').val()); }",
                    ),
                    components.HTML(id="result-2", tag="div", css_class="mt mb"),
                ]
            )
        ]


class TextInputView(CBAView):
    root = TextInputRoot
