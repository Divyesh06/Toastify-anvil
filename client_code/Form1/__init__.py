from ._anvil_designer import Form1Template
from anvil import *
from .. import toast

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def form_show(self, **event_args):
        toast.Toast("Your request was complete", style="success", timeout=5)