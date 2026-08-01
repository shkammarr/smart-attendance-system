import customtkinter as ctk
from PIL import Image
from GUI.theme import *


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            width=300,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.pack_propagate(False)

        # ==========================================
        # Logo
        # ==========================================

        try:
            logo = ctk.CTkImage(
                light_image=Image.open("Logo/logo.jpeg"),
                dark_image=Image.open("Logo/logo.jpeg"),
                size=(150, 150)
            )

            ctk.CTkLabel(
                self,
                image=logo,
                text=""
            ).pack(pady=(25, 15))

        except:
            ctk.CTkLabel(
                self,
                text="🤖",
                font=("Segoe UI Emoji", 70)
            ).pack(pady=(30, 15))

        # ==========================================
        # Title
        # ==========================================

        ctk.CTkLabel(
            self,
            text="SMART",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(anchor="w", padx=35)

        ctk.CTkLabel(
            self,
            text="ATTENDANCE",
            font=("Segoe UI", 28, "bold"),
            text_color="#39A9FF"
        ).pack(anchor="w", padx=35)

        ctk.CTkLabel(
            self,
            text="SYSTEM",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(anchor="w", padx=35)

        ctk.CTkFrame(
            self,
            width=90,
            height=3,
            fg_color="#39A9FF"
        ).pack(anchor="w", padx=35, pady=20)

        # ==========================================
        # Menu
        # ==========================================

        self.menu_button("🏠 Dashboard", True)
        self.menu_button("⚙ Settings")
        self.menu_button("ℹ About")

        # Push bottom card down
        ctk.CTkFrame(
            self,
            fg_color="transparent"
        ).pack(expand=True)

        # ==========================================
        # Bottom Card
        # ==========================================

        card = ctk.CTkFrame(
            self,
            width=240,
            height=120,
            fg_color="#102B57",
            corner_radius=18
        )

        card.pack(pady=25)
        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text="Secure • Smart • Reliable",
            font=("Segoe UI", 15, "bold"),
            text_color="#2DD4BF"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            card,
            text="AI Powered Face\nAttendance System",
            font=("Segoe UI", 13),
            text_color="white",
            justify="center"
        ).pack()

    # ==========================================
    # Sidebar Button
    # ==========================================

    def menu_button(self, text, active=False):

        color = PRIMARY if active else "transparent"

        button = ctk.CTkButton(

            self,

            text=text,

            width=235,

            height=48,

            fg_color=color,

            hover_color=HOVER,

            corner_radius=14,

            anchor="w",

            font=("Segoe UI", 16)

        )

        button.pack(pady=8)