import customtkinter as ctk

class SingleEntryFrame(ctk.CTkFrame):
    def __init__(self, master, header_name, name, text, default):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=20, pady=5)

        self.entry = ctk.CTkEntry(self)
        self.entry.insert(0, str(default))
        self.entry.grid(row=1, column=0, padx=20, pady=5)

    def get_value(self):
        try:
            return float(self.entry.get())
        except ValueError:
            return 1.5  # fallback
