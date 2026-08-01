import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(self, master, title, value, subtitle, color):

        super().__init__(
            master,
            width=270,
            height=170,
            fg_color="white",
            corner_radius=20,
            border_width=1,
            border_color="#E5E7EB"
        )

        self.pack_propagate(False)

        # Top Circle
        circle = ctk.CTkFrame(
            self,
            width=60,
            height=60,
            fg_color=color,
            corner_radius=30
        )
        circle.pack(pady=(15,8))

        circle.pack_propagate(False)

        ctk.CTkLabel(
            circle,
            text="●",
            font=("Arial",24),
            text_color="white"
        ).pack(expand=True)

        # Title
        ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI",15),
            text_color="#6B7280"
        ).pack()

        # Value
        self.valueLabel = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI",28,"bold"),
            text_color="#111827"
        )

        self.valueLabel.pack(pady=(5,0))

        # Subtitle
        ctk.CTkLabel(
            self,
            text=subtitle,
            font=("Segoe UI",13),
            text_color=color
        ).pack(side="bottom", pady=15)

    def update_value(self, value):
        self.valueLabel.configure(text=value)