import customtkinter as ctk
import csv
import os
from datetime import datetime

from GUI.theme import *


class RecentTable(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=18
        )

        # -------------------------
        # Title
        # -------------------------

        title = ctk.CTkLabel(
            self,
            text="Recent Attendance",
            font=("Segoe UI", 22, "bold"),
            text_color=TEXT
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20,10)
        )

        # -------------------------
        # Textbox
        # -------------------------

        self.box = ctk.CTkTextbox(
            self,
            height=240,
            font=("Consolas",15),
            fg_color="#F9FAFB",
            border_width=1,
            border_color="#E5E7EB"
        )

        self.box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        self.load_data()

    # ===================================

    def load_data(self):

        self.box.delete("1.0","end")

        folder = "Attendance"

        if not os.path.exists(folder):

            self.box.insert(
                "end",
                "No attendance records found."
            )

            self.box.configure(state="disabled")
            return

        today = datetime.now().strftime("%Y-%m-%d") + ".csv"

        file = os.path.join(folder,today)

        if not os.path.exists(file):

            self.box.insert(
                "end",
                "Today's attendance is empty."
            )

            self.box.configure(state="disabled")
            return

        self.box.insert(
            "end",
            f"{'ID':<10}{'NAME':<28}{'TIME'}\n"
        )

        self.box.insert(
            "end",
            "-"*55 + "\n"
        )

        with open(file,"r") as f:

            reader = csv.reader(f)

            next(reader,None)

            for row in reader:

                self.box.insert(

                    "end",

                    f"{row[0]:<10}{row[1]:<28}{row[3]}\n"

                )

        self.box.configure(state="disabled")