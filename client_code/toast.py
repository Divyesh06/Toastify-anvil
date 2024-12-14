from anvil import *
from .Toaster import Toaster
from anvil.js.window import document
from . import styles_data

class Toast:
    def __init__(self, message, style="info", timeout = 2, title=""): #Title is added just to migrate from Notifications and does not actually show
        toaster = Toaster()
        style=styles_data.styles[style]
        toaster.toaster_icon.style.fill = style['color']
        toaster.toaster_progress.style.background = style['color']
        toaster.toaster_text.innerText = message
        toaster.toaster_progress.style.animationDuration=f"{timeout}s"
      
        toaster.toaster_icon_path.setAttribute("d",style['icon'])
        document.body.appendChild(toaster.toaster)