import customtkinter as ctk
from datetime import datetime
from GUI.theme import *


class Header(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            height=110,
            fg_color="white",
            corner_radius=18
        )

        self.pack_propagate(False)

        # ==========================
        # Left Side
        # ==========================

        left = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        left.pack(side="left", padx=30, pady=18)

        ctk.CTkLabel(
            left,
            text="SMART ATTENDANCE SYSTEM",
            font=("Segoe UI",30,"bold"),
            text_color=TEXT
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text="AI Powered Face Recognition Attendance",
            font=("Segoe UI",14),
            text_color=SUBTEXT
        ).pack(anchor="w")

        # ==========================
        # Right Side
        # ==========================

        right = ctk.CTkFrame(
            self,
            fg_color="#F8FAFC",
            width=270,
            height=75,
            corner_radius=16
        )

        right.pack(side="right", padx=25)

        right.pack_propagate(False)

        self.date = ctk.CTkLabel(
            right,
            text="",
            font=("Segoe UI",14),
            text_color=SUBTEXT
        )

        self.date.pack(pady=(10,0))

        self.time = ctk.CTkLabel(
            right,
            text="",
            font=("Segoe UI",22,"bold"),
            text_color=PRIMARY
        )

        self.time.pack()

        self.update_time()

    # ==========================
    # Live Clock
    # ==========================

    def update_time(self):

        now = datetime.now()

        self.date.configure(
            text=now.strftime("%A, %d %B %Y")
        )

        self.time.configure(
            text=now.strftime("%I:%M:%S %p")
        )

        self.after(1000, self.update_time)