import customtkinter as ctk

class DropdownFrame(ctk.CTkFrame):
    def __init__(self, master, name, text, default, options):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=20, pady=5)

        self.option_menu = ctk.CTkOptionMenu(self, values=options)
        self.option_menu.set(default)
        self.option_menu.grid(row=1, column=0, padx=20, pady=5)

    def get_option(self):
        return self.option_menu.get()
