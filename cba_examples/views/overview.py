from __future__ import print_function, unicode_literals

from django.core.urlresolvers import reverse

from cba import components
from cba.base import CBAView


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
                            components.Link(text="Button", href=reverse("button")),
                            components.Link(text="Checkboxes", href=reverse("checkboxes")),
                            components.Link(text="Drag and Drop", href=reverse("drag_n_drop")),
                            components.Link(text="File Input 1", href=reverse("file_input_1")),
                            components.Link(text="File Input 2", href=reverse("file_input_2")),
                            components.Link(text="Radio buttons", href=reverse("radio")),
                            components.Link(text="Select 1", href=reverse("select_1")),
                            components.Link(text="Select 2", href=reverse("select_2")),
                            components.Link(text="Select 3", href=reverse("select_3")),
                            components.Link(text="Table 1", href=reverse("table_1")),
                            components.Link(text="Table 2", href=reverse("table_2")),
                            components.Link(text="Textarea 1", href=reverse("textarea_1")),
                            components.Link(text="Textarea 2", href=reverse("textarea_2")),
                            components.Link(text="Text input", href=reverse("text_input_1")),
                            components.Link(text="Text input with local javascript", href=reverse("text_input_2")),
                            components.Link(text="Text input with global javascript", href=reverse("text_input_2")),
                        ]
                    ),
                ]
            )
        ]


class OverviewView(CBAView):
    root = OverviewRoot
