import customtkinter as ctk

class SwitchesFrame(ctk.CTkFrame):
    def __init__(self, master, name, text1, text2, command_name1, command_name2):
        super().__init__(master)

        self.switch1 = ctk.CTkSwitch(self, text=text1, command=command_name1)
        self.switch1.grid(row=0, column=0, padx=20, pady=10)

        self.switch2 = ctk.CTkSwitch(self, text=text2, command=command_name2)
        self.switch2.grid(row=1, column=0, padx=20, pady=10)

    def get_state1(self):
        return "on" if self.switch1.get() else "off"

    def get_state2(self):
        return "on" if self.switch2.get() else "off"

    def reset_values(self):
        self.switch1.deselect()
        self.switch2.deselect()
