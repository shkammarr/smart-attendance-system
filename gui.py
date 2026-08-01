import customtkinter as ctk

from GUI.theme import *
from GUI.sidebar import Sidebar
from GUI.header import Header
from GUI.dashboard import Dashboard

# ------------------------------------
# Appearance
# ------------------------------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ------------------------------------
# Main Window
# ------------------------------------

root = ctk.CTk()

root.title("Smart Attendance System")
root.geometry("1550x900")
root.minsize(1250, 700)
root.configure(fg_color=BACKGROUND)

# ------------------------------------
# Sidebar
# ------------------------------------

sidebar = Sidebar(root)

sidebar.pack(
    side="left",
    fill="y"
)

# ------------------------------------
# Main Area
# ------------------------------------

main = ctk.CTkFrame(
    root,
    fg_color=BACKGROUND,
    corner_radius=0
)

main.pack(
    side="right",
    fill="both",
    expand=True
)

# ------------------------------------
# Header
# ------------------------------------

header = Header(main)

header.pack(
    fill="x",
    padx=25,
    pady=(20, 10)
)

# ------------------------------------
# Dashboard
# ------------------------------------

dashboard = Dashboard(main)

dashboard.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(0, 10)
)

# ------------------------------------
# Run Application
# ------------------------------------

root.mainloop()