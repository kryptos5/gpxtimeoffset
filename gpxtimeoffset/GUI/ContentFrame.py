import customtkinter

from Config import Config


class ContentFrame(customtkinter.CTkFrame):

    def __init__(self, master, title: str, text: str):
        super().__init__(master)
        self.defaultText = text
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        label = customtkinter.CTkLabel(master=self,
                                       text=title,
                                       fg_color="transparent")
        label.grid(row=0,
                   column=0,
                   padx=Config.DEFAULT_PADX,
                   pady=Config.DEFAULT_PADY_TOP,
                   sticky="w")

        font = customtkinter.CTkFont(family="Courier New")
        self.textbox = customtkinter.CTkTextbox(master=self,
                                                corner_radius=0,
                                                height=300,
                                                wrap="none",
                                                font=font)
        self.textbox.grid(row=1,
                          column=0,
                          padx=Config.DEFAULT_PADX,
                          pady=Config.DEFAULT_PADY_BOTTOM,
                          sticky="nsew")
        self.reset()
        self.textbox.configure(state="disabled")

    def showContent(self, content: str):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        self.textbox.insert((0.0), content)
        self.textbox.configure(state="disabled")

    def reset(self):
        self.showContent("")
