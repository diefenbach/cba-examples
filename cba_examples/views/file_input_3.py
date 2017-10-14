from __future__ import print_function, unicode_literals

from cba import components
from cba.base import CBAView


class File(object):
    def __init__(self, id, url):
        self.file = {"url": url}
        self.id = id


class FileInputRoot(components.Group):
    def init_components(self):
        images = [
            File(id=1, url="/static/images/test.png"),
        ]
        self.initial_components = [
            components.Group(
                css_class="ui form container",
                initial_components=[
                    components.HTML(tag="h1", content="File Input", css_class="mb mt"),
                    components.HTML(tag="p", content="Upload one file", css_class="mb"),
                    components.FileInput(
                        id="file",
                        icon="file",
                        icon_position="right",
                        label="File",
                        multiple=False,
                        existing_files=images,
                    ),
                    components.HTML(id="result", tag="div", css_class="mt mb"),
                    components.Button(id="button", value="OK", handler={"click": "server:handle_button"}),
                ]
            ),
        ]

    def handle_button(self):
        file = self.get_component("file")
        result = self.get_component("result")
        result.content = "You uploaded: {}<br />".format(file.value)
        result.content += "You deleted: {}".format([f for f in file.to_delete])
        result.refresh()


class FileInputView(CBAView):
    root = FileInputRoot
