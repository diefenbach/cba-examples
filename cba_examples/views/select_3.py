from __future__ import print_function, unicode_literals

from cba import components
from cba import layouts
from cba.views import CBAView


class SelectRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="container mbm",
                initial_components=[
                    components.HTML(tag="h1", content="Select", css_class="mb mt"),
                    components.HTML(
                        tag="p",
                        css_class="mb",
                        content="""One select box depends on the other""",
                    ),
                ],
            ),
            layouts.Grid(
                css_class="container",
                initial_components=[
                    layouts.Column(
                        width=8,
                        initial_components=[
                            components.Select(
                                id="select-1",
                                label="Operation Systems",
                                options=[
                                    {
                                        "name": "Please select!",
                                        "value": 1,
                                    },
                                    {
                                        "name": "macOS",
                                        "value": 2,
                                    },
                                    {
                                        "name": "Windows",
                                        "value": 3,
                                    },
                                ],
                                value=1,
                                handler={"change": "server:handle_changed"},
                            ),
                        ],
                    ),
                    layouts.Column(
                        width=8,
                        initial_components=[
                            components.Select(
                                id="select-2",
                                label="Versions",
                                disabled=True,
                            ),
                        ],
                    )
                ]
            )
        ]

    def handle_changed(self):
        select_1 = self.get_component("select-1")
        select_2 = self.get_component("select-2")


        if select_1.value == "1":
            select_2.label = "Versions"
            select_2.disabled = True
            select_2.options = []
        elif select_1.value == "2":
            select_2.label = "macOS Versions"
            select_2.disabled = False
            select_2.options = [
                {
                    "name": "El Capitan",
                    "value": 1,
                },
                {
                    "name": "Sierra",
                    "value": 2,
                },
            ]
        elif select_1.value == "3":
            select_2.label = "Windows Versions"
            select_2.disabled = False
            select_2.options = [
                {
                    "name": "Windows 8",
                    "value": 1,
                },
                {
                    "name": "Windows 10",
                    "value": 2,
                },
            ]

        select_2.refresh()


class SelectView(CBAView):
    root = SelectRoot
