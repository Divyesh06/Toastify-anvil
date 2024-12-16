from ._Toast import _Toast
from anvil.js.window import document, setTimeout
from anvil.js import window
from . import styles_data
import anvil

positions = {
    "top-right": {"animation": "bounceInRight"},
    "top-left": {"animation": "bounceInLeft"},
    "top-center": {"animation": "bounceInDown"},
    "bottom-left": {"animation": "bounceInLeft"},
    "bottom-right": {"animation": "bounceInRight"},
    "bottom-center": {"animation": "bounceInUp"},
}

swipe_dismiss_threshold = 200

for position in positions:
    container = document.createElement("div")
    container.className = f"toaster-container toaster-{position}"
    y, x = position.split("-")
    container.style.setProperty(y, "0")
    if x != "center":
        container.style.setProperty(x, "0")

    else:
        container.style.transform = "translateX(-50%)"
        container.style.left = "50%"

    container.style.alignItems = (
        "center" if x == "center" else "flex-end" if x == "right" else "flex-start"
    )
    document.body.appendChild(container)


class Toast:
    def __init__(
        self, message, style="info", timeout=2, title="", position="top-right"
    ):
        self.toast = _Toast()
        self.position = position
        self.timeout = timeout
        self.drag = False
        self.distance_covered = 0
        self.toast.toast.onclick = self.hide
        self.toast.toast_text.innerText = message
        self.set_style(style)
        self.toast.toast_progress.style.animationDuration = f"{self.timeout}s"
        self.toast.toast.style.animation = f"{positions[position]['animation']} 0.6s"
        self.show()
        self.disable_click = False
        self.toast.toast.onpointerdown = self._start_drag
        window.addEventListener("pointermove", self._drag_move)
        window.addEventListener("pointerup", self._end_drag)
        window.addEventListener("touchmove", self._drag_move_touch)
        window.addEventListener("touchend", self._end_drag)

    def _start_drag(self, e):
        self.x = self.toast.toast.getBoundingClientRect().x
        self.drag = True

    def _drag_move_touch(self, e):
        self._drag_move(e.touches[0])

    def _drag_move(self, e):
        if self.drag:
            self.disable_click = True
            self.distance_covered = abs(self.x - e.clientX)
            self.toast.toast.style.opacity = (
                1 - self.distance_covered / swipe_dismiss_threshold
            )
            if "right" in self.position:
                self.toast.toast.style.right = (
                    f"{window.innerWidth - e.clientX - 100}px"
                )
            elif "right" in self.position:
                self.toast.toast.style.left = f"{e.clientX - 100}px"

            elif "center" in self.position:
                self.toast.toast.style.right = (
                    f"{window.innerWidth*0.5 - e.clientX - 100}px"
                )

    def _end_drag(self, e):
        self.drag = False
        if self.distance_covered > swipe_dismiss_threshold:
            self.toast.toast.remove()
        else:
            self.toast.toast.style.opacity = 1
            self.toast.toast.style.left = "initial"
            self.toast.toast.style.right = "initial"
        import time

        time.sleep(0.1)
        self.disable_click = False

    def _end_drag_touch(self, e):
        self._end_drag(e.touches[0])

    def show(self):
        container = document.getElementsByClassName(f"toaster-{self.position}")[0]
        container.appendChild(self.toast.toast)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return

    def update(self, style=None, message=None):
        if style:
            self.set_style(style)
        if message:
            self.toast.toast_text.innerText = message

    def hide(self, *args):
        import time
        
        if not self.disable_click:
            exit_animation = positions[self.position]["animation"].replace("In", "Out")

            if "Up" in exit_animation:
                exit_animation = exit_animation.replace("Up", "Down")
            elif "Down" in exit_animation:
                exit_animation = exit_animation.replace("Down", "Up")

            self.toast.toast.style.animation = f"{exit_animation} 0.8s"
            
            def remove_toast(*args):
                self.toast.toast.remove()

            time.sleep(0.8)
            remove_toast()
            #self.toast.toast.onanimationend = remove_toast

    def set_style(self, style):
        if style != "loading":
            self.toast.toast_progress.style.display = "block"
            self.toast.toast_loading.style.display = "none"
            self.toast.toast_icon.style.display = "flex"
            style = styles_data.styles[style]
            self.toast.toast_icon.style.fill = style["color"]
            self.toast.toast_progress.style.background = style["color"]
            self.toast.toast_icon_path.setAttribute("d", style["icon"])
            setTimeout(self.hide, self.timeout * 1000)

        else:
            self.toast.toast_icon.style.display = "none"
            self.toast.toast_loading.style.display = "block"
            self.toast.toast_progress.style.display = "none"


def patch_anvil_notifications():
    anvil.Notification = Toast
