import customtkinter as ctk


class ButtonWithLabel(ctk.CTkFrame):
    def __init__(self, *args, width, height, label, save_callback, button_text, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.columnconfigure((1), weight=1)
        self.columnconfigure((0, 2), weight=0)

        self.label = ctk.CTkLabel(self, text=label, width=100, anchor="w")
        self.label.grid(row=0, column=0, padx=(5, 5), pady=5, sticky="W")

        self.entry = ctk.CTkEntry(
            self, width=360, placeholder_text=f"add {label} here")
        self.entry.grid(row=0, column=1, padx=(5, 5), pady=5, sticky="E")

        self.save_cb = save_callback
        self.button = ctk.CTkButton(
            self, text=button_text if button_text else "Save", width=40, command=lambda: self.call_save_callback())
        self.button.grid(row=0, column=2, padx=(5, 5), pady=5)

    def call_save_callback(self):
        self.save_cb(self.entry.get())
        self.master.focus()

    def set_value(self, val):
        self.entry.delete(0, len(self.entry.get()))
        self.entry.insert(0, val)


class Metadata(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 550,
                 height: int = 140,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.data = {
            "AlbumName": '',
            "Artist": '',
        }

        self.title = ctk.CTkLabel(self, text="Album Metadata:")
        self.title.place(x=10, y=5)

        self.album_name = ButtonWithLabel(
            self, width=200, height=30, label="Album Title", save_callback=lambda e: self.set_data('AlbumName', e), button_text="Save")
        self.album_name.place(x=10, y=40)

        self.artist_name = ButtonWithLabel(
            self, width=200, height=30, label="Artist", save_callback=lambda e: self.set_data('Artist', e), button_text="Save")
        self.artist_name.place(x=10, y=85)

    def set_data(self, key, val):
        self.data[f'{key}'] = val


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.resizable(False, False)
        self.title("Record Tool")

        self.meta = Metadata(self)
        self.meta.place(x=25, y=100)


app = App()
app.mainloop()
