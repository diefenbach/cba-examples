from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class MyTableDataProvider(components.TableDataProvider):
    def __init__(self):
        super(MyTableDataProvider, self).__init__()
        for x in xrange(1, 20):
            self.data.append(
                {
                    "id": "col-{}".format(x),
                    "css_class": "clickable",
                    "handler": {"click": "server:handle_select_row"},
                    "data": [
                        "Name {}".format(x),
                        20 + x,
                        "Developer",
                    ]
                }
            )

    def get_headers(self):
        return ["Name", "Age", "Profession"]


class TableRoot(components.Group):
    def init_components(self):
        table = components.Table(
            id="table",
            data_provider=MyTableDataProvider(),
        )

        table.load_data()

        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="Table with data provider", css_class="mb mt"),
                    table,
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                    components.Button(id="button", value="OK", handler={"click": "server:handle_button"}),
                ]
            ),
        ]

    def handle_select_row(self):
        table = self.get_component("table")
        for row in table.components:
            row.selected = False

        row = self.get_component(self.component_id)
        row.selected = True

        table.refresh()

    def handle_button(self):
        table = self.get_component("table")
        rows = table.get_selected_rows()

        result = self.get_component("result")
        result.content = ", ".join([r.components[0].content for r in rows])
        result.refresh()


class TableView(CBAView):
    root = TableRoot
