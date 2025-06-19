import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.resizable(False, False)
        self.title("Record Tool")


app = App()
app.mainloop()
