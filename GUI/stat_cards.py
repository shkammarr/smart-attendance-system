import customtkinter as ctk

from GUI.theme import *


class StatCard(ctk.CTkFrame):

    def __init__(self, master, title, value, color):

        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=18,
            width=260,
            height=150
        )

        self.pack_propagate(False)

        # Top Color Strip
        strip = ctk.CTkFrame(
            self,
            fg_color=color,
            height=6,
            corner_radius=18
        )
        strip.pack(fill="x")

        # Title
        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 15),
            text_color=SUBTEXT
        )

        self.title.pack(
            pady=(18, 8)
        )

        # Value
        self.value = ctk.CTkLabel(
            self,
            text=str(value),
            font=("Segoe UI", 32, "bold"),
            text_color=color
        )

        self.value.pack()

        # Footer
        self.footer = ctk.CTkLabel(
            self,
            text="Updated Live",
            font=("Segoe UI", 12),
            text_color="#9CA3AF"
        )

        self.footer.pack(
            pady=(10, 0)
        )

    def update_value(self, value):
        self.value.configure(text=str(value))