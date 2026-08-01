import os
import csv
from datetime import datetime

import customtkinter as ctk

from GUI.theme import *
from GUI.stat_cards import StatCard
from GUI.action_cards import ActionCard
from GUI.recent_table import RecentTable


DATABASE = "Database/persons.csv"
MODEL = "Trainer/trainer.yml"


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=BACKGROUND
        )

        self.build_stats()
        self.build_actions()
        self.build_table()

    # ===================================
    # Statistics
    # ===================================

    def build_stats(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=(15,10)
        )

        self.persons = StatCard(
            frame,
            "Registered Persons",
            self.total_persons(),
            PRIMARY
        )

        self.persons.pack(side="left", padx=10)

        self.attendance = StatCard(
            frame,
            "Today's Attendance",
            self.today_attendance(),
            SUCCESS
        )

        self.attendance.pack(side="left", padx=10)

        self.date = StatCard(
            frame,
            "Today's Date",
            datetime.now().strftime("%d %b %Y"),
            PURPLE
        )

        self.date.pack(side="left", padx=10)

        self.model = StatCard(
            frame,
            "Model Status",
            self.model_status(),
            WARNING
        )

        self.model.pack(side="left", padx=10)

    # ===================================
    # Action Cards
    # ===================================

    def build_actions(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(
            pady=20
        )

        # Row 1

        row1 = ctk.CTkFrame(frame, fg_color="transparent")
        row1.pack()

        ActionCard(
            row1,
            "👤",
            "Register",
            "Add New Face",
            PRIMARY,
            lambda: os.system("python register_person.py")
        ).pack(side="left", padx=10)

        ActionCard(
            row1,
            "🎓",
            "Train",
            "Build Model",
            WARNING,
            lambda: os.system("python train_model.py")
        ).pack(side="left", padx=10)

        ActionCard(
            row1,
            "📷",
            "Attendance",
            "Mark Attendance",
            SUCCESS,
            lambda: os.system("python attendance.py")
        ).pack(side="left", padx=10)

        ActionCard(
            row1,
            "📊",
            "Reports",
            "View Reports",
            PURPLE,
            lambda: os.system("python attendance_report.py")
        ).pack(side="left", padx=10)

        # Row 2

        row2 = ctk.CTkFrame(frame, fg_color="transparent")
        row2.pack(pady=15)

        ActionCard(
            row2,
            "👥",
            "Persons",
            "View Users",
            "#0EA5E9",
            lambda: os.system("python view_persons.py")
        ).pack(side="left", padx=10)

        ActionCard(
            row2,
            "✏",
            "Edit",
            "Update Details",
            "#EC4899",
            lambda: os.system("python edit_person.py")
        ).pack(side="left", padx=10)

        ActionCard(
            row2,
            "🗑",
            "Delete",
            "Remove User",
            RED,
            lambda: os.system("python delete_person.py")
        ).pack(side="left", padx=10)

        ActionCard(
            row2,
            "🚪",
            "Exit",
            "Close App",
            "#64748B",
            self.master.master.destroy
        ).pack(side="left", padx=10)

    # ===================================
    # Recent Attendance
    # ===================================

    def build_table(self):

        table = RecentTable(self)

        table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

    # ===================================
    # Helpers
    # ===================================

    def total_persons(self):

        if not os.path.exists(DATABASE):
            return 0

        with open(DATABASE) as f:
            return max(0, len(list(csv.reader(f))) - 1)

    def today_attendance(self):

        folder = "Attendance"

        today = datetime.now().strftime("%Y-%m-%d") + ".csv"

        file = os.path.join(folder, today)

        if not os.path.exists(file):
            return 0

        with open(file) as f:
            return max(0, len(list(csv.reader(f))) - 1)

    def model_status(self):

        if os.path.exists(MODEL):
            return "READY"

        return "NOT TRAINED"