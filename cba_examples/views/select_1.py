from __future__ import print_function, unicode_literals

from cba import components
from cba.views import CBAView


class SelectRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="container",
                initial_components=[
                    components.HTML(tag="h1", content="Select", css_class="mb mt"),
                    components.HTML(
                        tag="p",
                        css_class="mb",
                        content="""Select exactly one entry. Every time the
                                   selection changes, the value is sent to the server""",
                    ),
                    components.Select(
                        id="select",
                        options=[
                            {
                                "name": "One",
                                "value": 1,
                            },
                            {
                                "name": "Two",
                                "value": 2,
                            },
                            {
                                "name": "Three",
                                "value": 3,
                            },
                        ],
                        value=2,
                        handler={"change": "server:handle_changed"},
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                ]
            )
        ]

    def handle_changed(self):
        select = self.get_component("select")
        result = self.get_component("result")

        result.content = "You selected: {}".format(select.value)
        result.refresh()


class SelectView(CBAView):
    root = SelectRoot
