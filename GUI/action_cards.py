import customtkinter as ctk


class ActionCard(ctk.CTkFrame):

    def __init__(self, master, icon, title, subtitle, color, command):

        super().__init__(
            master,
            width=240,
            height=170,
            fg_color="white",
            corner_radius=20,
            border_width=1,
            border_color="#E5E7EB"
        )

        self.pack_propagate(False)

        self.command = command
        self.normal = "white"
        self.hover = "#F8FAFC"

        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)
        self.bind("<Button-1>", lambda e: self.command())

        # --------------------
        # Icon Circle
        # --------------------

        circle = ctk.CTkFrame(
            self,
            width=60,
            height=60,
            fg_color=color,
            corner_radius=30
        )

        circle.pack(pady=(18,8))
        circle.pack_propagate(False)

        icon_label = ctk.CTkLabel(
            circle,
            text=icon,
            font=("Segoe UI Emoji",28)
        )

        icon_label.place(relx=0.5,rely=0.5,anchor="center")

        # --------------------

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI",18,"bold"),
            text_color="#111827"
        )

        title_label.pack()

        subtitle_label = ctk.CTkLabel(
            self,
            text=subtitle,
            font=("Segoe UI",13),
            text_color="#6B7280"
        )

        subtitle_label.pack(pady=(5,0))

        # Hover for children

        for widget in [
            circle,
            icon_label,
            title_label,
            subtitle_label
        ]:
            widget.bind("<Enter>", self.enter)
            widget.bind("<Leave>", self.leave)
            widget.bind("<Button-1>", lambda e: self.command())

    # --------------------

    def enter(self, event):

        self.configure(
            fg_color=self.hover,
            border_color="#3B82F6"
        )

    def leave(self, event):

        self.configure(
            fg_color=self.normal,
            border_color="#E5E7EB"
        )