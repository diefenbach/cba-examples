from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class FileInputRoot(components.Group):
    def init_components(self):
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="File Input", css_class="mb mt"),
                    components.HTML(tag="p", content="Upload multiple files", css_class="mb"),
                    components.FileInput(
                        id="file",
                        icon="file",
                        icon_position="right",
                        label="File",
                        multiple=True,
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                    components.Button(id="button", value="OK", handler={"click": "server:handle_button"}),
                ]
            ),
        ]

    def handle_button(self):
        file = self.get_component("file")
        result = self.get_component("result")
        result.content = "You uploaded: {}".format([f.name for f in file.value])
        result.refresh()


class FileInputView(CBAView):
    root = FileInputRoot
