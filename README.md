# Toastify for Anvil

Inspired By [React-toastify](https://fkhadra.github.io/react-toastify/introduction/), I decided to create something similar for Anvil. Toast components can be a beautiful replacement for default Anvil Notifications

___
Test Playground to test it out https://anvil-toastify.anvil.app/

Clone Link: https://anvil.works/build#clone:KW3ZQNP7C5I5MMZQ=LNH6TDTWKQEG5G4P2G7XUVC4

___

**Usage**

```python
from toastify import toastify
toastify.Toast("Hello World", style="info", timeout = 5, position = "top-right")
With Server Calls

with toastify.Toast("Making call to Server", style="loading") as toast:
    try:
        anvil.server.call_s('get_data_from_server')
        toast.update("success","Data fetched from Server")
    except:
        toast.update("danger","Failed to Fetch Data from Server")
```

## 🍞 Toast API Reference

### Toast Parameters

| Parameter   | Description                                                                 | Accepted Values                                                                 | Default      |
|-------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------|
| `message`   | The text to display in the toast.                                            | *String*                                                                         | —            |
| `style`     | Style of the toast.                                                         | `success`, `info`, `warning`, `danger`, `loading`                               | `info`       |
| `position`  | Position of the toast on the screen.                                        | `top-left`, `top-right`, `top-center`, `bottom-left`, `bottom-right`, `bottom-center` | `top-right` |
| `timeout`   | Duration (in seconds) the toast will be shown.                              | *Number (seconds)*                                                               | `2`          |

### Toast Methods

- `hide()`  
  Hides the toast manually.

- `update(new_style, new_text)`  
  Updates an existing toast’s style and message.

---

## 🎁 Extra Features

- Smooth **animation** on entry and exit.
- **Progress bar** indicating the time remaining (based on `timeout`).
- **Swipe to dismiss** (mobile-friendly).
  
---

## 🔁 Replacing Notifications with Toasts

Since `Toast` accepts the same parameters as Anvil's `Notification`, you can easily switch between them:

```python
# With Notification
with Notification("Doing Operation", style="info", timeout=4):
    ...

# With Toast
with toastify.Toast("Doing Operation", style="info", timeout=4):
    ...
```

## 🔧 Patching Notifications (Optional)

If you'd prefer not to change all `Notification` references manually, you can patch Anvil's built-in `Notification` component to use `Toast` instead:

```python
from toastify import toastify

# Call this once during your app's startup (e.g., in the startup form/module)
toastify.patch_anvil_notifications()

# IMPORTANT: Ensure this comes *before* importing anything from Anvil
from anvil import *
```

> **⚠️ Warning:** This approach will override Anvil’s default Notification behavior across the entire app. As a result, the original Anvil Notification component will no longer be available. Use with caution.
