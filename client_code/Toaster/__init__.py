from ._anvil_designer import ToasterTemplate
from anvil import *


class Toaster(ToasterTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.toaster = self.dom_nodes['toaster']
        self.toaster_icon = self.dom_nodes['toaster-icon']
        self.toaster_text = self.dom_nodes['toaster-text']
        self.toaster_icon_path= = self.dom_nodes['toaster-icon-path']
        