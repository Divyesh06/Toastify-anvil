from ._anvil_designer import _ToastTemplate
from anvil import *


class _Toast(_ToastTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.toast = self.dom_nodes['toast']
        self.toast_icon = self.dom_nodes['toast-icon']
        self.toast_text = self.dom_nodes['toast-text']
        self.toast_icon_path = self.dom_nodes['toast-icon-path']
        self.toast_progress = self.dom_nodes['toast-progress']
        self.toast_loading = self.dom_nodes['toast-loading']
        self.toast_close = self.dom_nodes['toast-close']
        