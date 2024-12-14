from anvil import *
from .Toaster import Toaster
from anvil.js.window import document, setTimeout
from . import styles_data

positions = {
    'top-right': {"animation": "bounceInRight"},
    'top-left': {"animation": "bounceInLeft"},
    'top-center': {"animation": "bounceInDown"},
    'bottom-left': {"animation": "bounceInLeft"},
    'bottom-right': {"animation": "bounceInRight"},
    'bottom-center': {"animation": "bounceInUp"}
}

for position in positions:
    container = document.createElement("div")
    container.className=f"toaster-container toaster-{position}"
    y,x = position.split("-")
    container.style.setProperty(y,"0")
    if x!="center":
        container.style.setProperty(x,"0")
        
    else:
        container.style.transform="translateX(-50%)"
        container.style.left="50%"

    container.style.alignItems = "center" if x=="center" else "flex-end" if x=="right" else "flex-start"
    document.body.appendChild(container)

class Toast:
    def __init__(self, message, style="info", timeout = 2, title="", close_on_exit=False,position="top-right"): #Title is added just to migrate from Notifications and does not actually show
        self.toaster = Toaster()  
        self.close_on_exit = close_on_exit
        self.timeout=timeout
        self.toaster.toaster_text.innerText = message
        self.set_style(style)
        self.toaster.toaster_progress.style.animationDuration=f"{self.timeout}s"
        self.toaster.toaster.style.animation=f"{positions[position]['animation']} 0.6s"
        container = document.getElementsByClassName(f"toaster-{position}")[0]
        container.appendChild(self.toaster.toaster)
        
        
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self.close_on_exit:
            self.close()
        
    def update(self,style=None,message=None):
        if style:
            self.set_style(style)
        if message:
            self.toaster.toaster_text.innerText=message

    def close(self, *args):
        self.toaster.toaster.style.animation = "bounceOutRight 0.6s"
        
        def remove_toaster(*args):
            self.toaster.toaster.remove()

        self.toaster.toaster.onanimationend=remove_toaster
    
    def set_style(self,style):
        if style!="loading":
            self.toaster.toaster_progress.style.display="block"
            self.toaster.toaster_loading.style.display="none"
            self.toaster.toaster_icon.style.display="flex"
            style=styles_data.styles[style]
            self.toaster.toaster_icon.style.fill = style['color']
            self.toaster.toaster_progress.style.background = style['color']
            self.toaster.toaster_icon_path.setAttribute("d",style['icon'])
            setTimeout(self.close, self.timeout * 1000)
            
        else:
            self.toaster.toaster_icon.style.display="none"
            self.toaster.toaster_loading.style.display="block"
            self.toaster.toaster_progress.style.display="none"