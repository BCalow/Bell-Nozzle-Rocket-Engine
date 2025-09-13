#import initialVariablesCalculations
import customtkinter as ctk


class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.title("Bell Nozzle Rocket Engine Initial Variables")

        #Data Entry Sections
        self.M = self.dataEntry(self, "Molar Mass", "Kg/Mol", 0)
        self.m_p = self.dataEntry(self, "Propellent Mass", "Kg", 1)
        self.dt = self.dataEntry(self, "Burn Time", "S", 2)
        self.T_c = self.dataEntry(self, "Chamber Temperature", "°C", 3)
        self.gamma = self.dataEntry(self, "Ratio of Specific Heats", "", 4)
        self.A_e = self.dataEntry(self, "Nozzle Exit Area", "m²", 5)
        self.P_a = self.dataEntry(self, "Ambient Pressure", "kPa", 6)

        #Run Analysis Button
        self.runAnalysis = ctk.CTkButton(self, text="Run Analysis", corner_radius=0)
        self.runAnalysis.grid(row=7, column=0, padx=20, pady=20, columnspan=3, sticky="w")

    def disableSection(self):
        self.entry.configure(state="disabled", fg_color=("#151515", "#0C0C0C"), text_color=("#555555"), textvariable="")
        self.name.configure(text_color=("#666666"))
        self.unit.configure(text_color=("#666666"))

    class dataEntry(ctk.CTkFrame):
        def __init__(self, master, name, unit, row):
            super().__init__(master)

            self.checkbox_state = ctk.StringVar(value="off")
            self.checkbox = ctk.CTkCheckBox(master, text="", variable=self.checkbox_state, onvalue="on", offvalue="off")
            self.checkbox.grid(row=row, column=0, padx=(20, 5), pady=5)

            self.name = ctk.CTkLabel(master, text=name)
            self.name.grid(row=row, column=1, padx=(5, 5), pady=5)

            self.entry = ctk.CTkEntry(master, width=75)
            self.entry.grid(row=row, column=2, padx=(5, 5), pady=5)

            self.unit = ctk.CTkLabel(master, text=unit)
            self.unit.grid(row=row, column=3, padx=(0, 5), pady=5, sticky="w")

            def get_values(self):
                return self.entry.get()


app = app()
app.mainloop()