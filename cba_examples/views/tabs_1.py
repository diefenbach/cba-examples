from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class TabsRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                initial_components=[
                    components.HTML(tag="h1", content="Tabs", css_class="mb mt"),
                    components.Tab(
                        initial_components=[
                            components.TabItem(
                                title="Eins",
                                id="tab-1",
                                is_grid=True,
                                active=True,
                                handler={"load": "server:handle_load|history"},
                                initial_components=[
                                    components.TextInput(id="first_name", label="First Name", cols="eight", handler={"keyup": "server:handle_button:13"}),
                                    components.TextInput(id="last_name", label="Last Name", cols="eight", handler={"keyup": "server:handle_button:13"}),
                                    components.TextInput(id="zip_code", label="ZIP Code", cols="five", handler={"keyup": "server:handle_button:13"}),
                                    components.TextInput(id="city", label="City", cols="eleven", handler={"keyup": "server:handle_button:13"}),
                                    components.TextInput(id="fon", label="Fon", cols="five", handler={"keyup": "server:handle_button:13"}),
                                    components.TextInput(id="mobile", label="Mobile", cols="five", handler={"keyup": "server:handle_button:13"}),
                                    components.TextInput(id="e-mail", label="E-Mail", cols="six", handler={"keyup": "server:handle_button:13"}),
                                    components.Button(id="button", value="Save", cols="twelve", handler={"click": "server:handle_button"}),
                                ],
                            ),
                            components.TabItem(
                                id="tab-2",
                                title="Zwei",
                                handler={"load": "server:handle_load|history"},
                            ),
                        ]
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                ]
            ),
        ]

    def handle_load(self):
        tab_item = self.get_component(self.component_id)
        for ti in tab_item.parent.components:
            ti.active = False
        tab_item.active = True

    def handle_button(self):
        form = self.get_component("tab-1")

        content = ""

        for component in form.components:
            if not isinstance(component, components.TextInput):
                continue

            content += " " + component.value

        result = self.get_component("result")
        result.content = content

        form.refresh()
        result.refresh()


class TabsView(CBAView):
    root = TabsRoot
