from __future__ import print_function, unicode_literals

from cba import components
from cba.views import CBAView


class SelectRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="container",
                initial_components=[
                    components.HTML(tag="h1", content="Multipe select box with optinal new entries.", css_class="mb mt"),
                    components.HTML(
                        tag="p",
                        css_class="mb",
                        content="""Select one or more entries or add a new one.
                                   Every time the selection changes, the values are sent to the server""",
                    ),
                    components.Select(
                        id="select",
                        multiple=True,
                        allow_additions = True,
                        options=[
                            {
                                "name": "One",
                                "value": "One",
                            },
                            {
                                "name": "Two",
                                "value": "Two",
                            },
                            {
                                "name": "Three",
                                "value": "Three",
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
