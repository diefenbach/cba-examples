from __future__ import print_function, unicode_literals

from django.core.urlresolvers import reverse

from cba import components
from cba.views import CBAView


class OverviewRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container mt",
                initial_components=[
                    components.HTML(tag="h1", content="CBA Examples Overview", css_class="mb"),
                    components.List(
                        type="ul",
                        initial_components=[
                            components.Link(text="Checkboxes", href=reverse("checkboxes")),
                            components.Link(text="Radio buttons", href=reverse("radio")),
                            components.Link(text="Text input", href=reverse("text_input_1")),
                            components.Link(text="Text input with local javascript", href=reverse("text_input_2")),
                            components.Link(text="Text input with global javascript", href=reverse("text_input_2")),
                            components.Link(text="Drag and Drop", href=reverse("drag_n_drop")),
                            components.Link(text="Select", href=reverse("select_1")),
                        ]
                    ),
                ]
            )
        ]


class OverviewView(CBAView):
    root = OverviewRoot
