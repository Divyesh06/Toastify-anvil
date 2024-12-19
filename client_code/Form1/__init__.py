from ._anvil_designer import Form1Template
from anvil import *
from .. import toastify

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        toastify.Toast("Hello")