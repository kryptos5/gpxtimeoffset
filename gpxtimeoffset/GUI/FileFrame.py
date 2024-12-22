import os
from tkinter import filedialog

import customtkinter
from Config import Config


class FileFrame(customtkinter.CTkFrame):

    def __init__(self, master, openFileCallback):
        super().__init__(master)
        self.openFileCallback = openFileCallback
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)

        label = customtkinter.CTkLabel(master=self,
                                       text="File",
                                       fg_color="transparent")
        label.grid(row=0,
                   column=0,
                   padx=Config.DEFAULT_PADX_LEFT,
                   pady=Config.DEFAULT_PADY,
                   sticky="w")

        self.textbox = customtkinter.CTkTextbox(master=self,
                                                corner_radius=0,
                                                height=Config.DEFAULT_HEIGHT)
        self.textbox.grid(row=0,
                          column=1,
                          padx=Config.DEFAULT_PADX_MIDDLE,
                          pady=Config.DEFAULT_PADY,
                          sticky="we")

        btnSelect = customtkinter.CTkButton(master=self,
                                            text="Select",
                                            command=self.browseFile)
        btnSelect.grid(row=0,
                       column=2,
                       padx=Config.DEFAULT_PADX_RIGHT,
                       pady=Config.DEFAULT_PADY)

    def browseFile(self):
        fileTypes = (("gpx files", "*.gpx"), ("All files", "*.*"))
        filename = filedialog.askopenfilename(title="Select a gpx file",
                                              initialdir=os.getcwd() +
                                              "../gpxsamples",
                                              filetypes=fileTypes)
        if len(filename) == 0:
            return
        self.textbox.delete("0.0", "end")
        self.textbox.insert((0.0), filename)
        self.openFileCallback(filename)
