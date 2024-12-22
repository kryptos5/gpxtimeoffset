import customtkinter

from Config import Config


class MessageBox(customtkinter.CTkToplevel):

    def __init__(self, parent: customtkinter.CTk, message: str, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.moveToCenter()
        self.title(Config.APP_NAME)
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = customtkinter.CTkLabel(self, text=message)
        label.grid(row=0, column=0)

        button = customtkinter.CTkButton(self, text="OK", command=self.close)
        button.grid(row=1,
                    column=0,
                    padx=Config.DEFAULT_PADX,
                    pady=Config.DEFAULT_PADY_BOTTOM,
                    sticky="e")

        self.grab_set()

    def moveToCenter(self):
        self.wait_visibility()
        x = self.parent.winfo_x() + int(self.parent.winfo_width() / 2) - int(
            Config.MESSAGE_BOX_DEFAULT_WIDTH / 2)
        y = self.parent.winfo_y() + int(self.parent.winfo_height() / 2) - int(
            Config.MESSAGE_BOX_DEFAULT_HEIGHT / 2)

        self.geometry(
            f"{Config.MESSAGE_BOX_DEFAULT_WIDTH}x{Config.MESSAGE_BOX_DEFAULT_HEIGHT}+{x}+{y}"
        )

    def close(self):
        self.destroy()
