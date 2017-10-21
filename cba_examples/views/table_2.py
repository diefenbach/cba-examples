from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class TableRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="Table without data provider", css_class="mb mt"),
                    components.Table(
                        id="table",
                        headers=("Name", "Age", "Profession"),
                        initial_components=[
                            components.TableRow(
                                handler={"click": "server:handle_select_row"},
                                initial_components=[
                                    components.TableColumn(content="Name 1"),
                                    components.TableColumn(content="21"),
                                    components.TableColumn(content="Developer"),
                                ]
                            ),
                            components.TableRow(
                                handler={"click": "server:handle_select_row"},
                                initial_components=[
                                    components.TableColumn(content="Name 2"),
                                    components.TableColumn(content="22"),
                                    components.TableColumn(content="Developer"),
                                ]
                            ),
                            components.TableRow(
                                handler={"click": "server:handle_select_row"},
                                initial_components=[
                                    components.TableColumn(content="Name 3"),
                                    components.TableColumn(content="23"),
                                    components.TableColumn(content="Developer"),
                                ]
                            ),
                        ],
                    ),
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
