from __future__ import print_function, unicode_literals

from cba import components
from cba.views import CBAView


class DragnDropRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(
                        tag="h1",
                        content="Drag'n Drop",
                        css_class="mb mt"
                    ),
                    components.HTML(
                        content="The drop event is handled by the server."
                    ),
                    components.HTML(
                        id="draggable",
                        tag="div",
                        content="Draggable",
                        draggable=True,
                        css_class="mb mt",
                        attributes={"style": "width:180px; padding:20px; background: red"}

                    ),
                    components.HTML(
                        id="droppable",
                        tag="div",
                        css_class="mt mb",
                        droppable=True,
                        content="Droppable",
                        handler={"drop": "server:handle_drop"},
                        attributes={"style": "padding:10px; width:200px; height:200px; background: blue"}
                    ),
                ]
            ),
        ]

    def handle_drop(self):
        draggable = self.get_component(self.source_id)
        droppable = self.get_component("droppable")
        group = draggable.parent

        group.remove_component("draggable")
        droppable.add_component(draggable)

        group.refresh()


class DragnDropView(CBAView):
    root = DragnDropRoot
