from __future__ import print_function, unicode_literals

from cba import components
from cba.views import CBAView


class TableRoot(components.Group):
    def init_components(self):
        table = components.Table(
            id="table",
            headers=["Name", "Age", "Profession"],
        )

        for x in range(1, 10):
            table.add_component(
                components.TableRow(
                    initial_components=[
                        components.TableColumn(
                            initial_components=[
                                components.HTML(content="Name {}".format(x))
                            ],
                        ),
                        components.TableColumn(initial_components=[
                                components.HTML(content=x*10)
                            ],
                        ),
                        components.TableColumn(initial_components=[
                                components.HTML(content="Developer {}".format(x))
                            ],
                        ),
                    ]
                )
            )

        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="Table", css_class="mb mt"),
                    table,
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                    components.Button(id="button-1", value="OK", handler={"click": "server:handle_button"}),
                ]
            ),
        ]


class TableView(CBAView):
    root = TableRoot
