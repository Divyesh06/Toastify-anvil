from ._anvil_designer import PlaygroundTemplate
from anvil import *
from .. import toastify


class Playground(PlaygroundTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        

    def button_1_click(self, **event_args):
        toastify.Toast(
            self.text_box_1_copy.text,
            style=self.drop_down_1_copy.selected_value,
            timeout=self.text_box_1.text,
            position=self.drop_down_1.selected_value,
        )
