import os
from tkinter import filedialog

import customtkinter

from Config import Config


class SettingsFrame(customtkinter.CTkFrame):

    def __init__(self, master, applySettingsCallback, saveFileCallback):
        super().__init__(master)
        self.applySettingsCallback = applySettingsCallback
        self.saveFileCallback = saveFileCallback
        self.grid_rowconfigure(0, weight=0)

        column = 0
        label = customtkinter.CTkLabel(master=self,
                                       text="Time Offset",
                                       fg_color="transparent")
        label.grid(row=0,
                   column=column,
                   padx=Config.DEFAULT_PADX_LEFT,
                   pady=Config.DEFAULT_PADY,
                   sticky="w")
        column += 1

        self.textboxHours, column = self.addTimeUI(column, "1", "hour(s)")
        self.textboxMinutes, column = self.addTimeUI(column, "00", "minute(s)")
        self.textboxSeconds, column = self.addTimeUI(column, "00", "second(s)")

        self.btnApply = customtkinter.CTkButton(master=self,
                                                text="Apply",
                                                command=self.applySettings)
        self.btnApply.grid(row=0,
                           column=column,
                           padx=Config.DEFAULT_PADX_MIDDLE,
                           pady=Config.DEFAULT_PADY)
        self.enableApply(False)
        column += 1

        self.btnSave = customtkinter.CTkButton(master=self,
                                               text="Save",
                                               command=self.saveFile)
        self.btnSave.grid(row=0,
                          column=column,
                          padx=Config.DEFAULT_PADX_MIDDLE,
                          pady=Config.DEFAULT_PADY)
        self.enableSave(False)

    def applySettings(self):
        offsetHours = int(self.textboxHours.get(0.0, "end"))
        offsetMinutes = int(self.textboxMinutes.get(0.0, "end"))
        offsetSeconds = int(self.textboxSeconds.get(0.0, "end"))
        self.applySettingsCallback(offsetHours=offsetHours,
                                   offsetMinutes=offsetMinutes,
                                   offsetSeconds=offsetSeconds)

    def saveFile(self):
        fileTypes = (("gpx files", "*.gpx"), ("All files", "*.*"))
        filename = filedialog.asksaveasfilename(title="Save modified gpx file",
                                                initialdir=os.getcwd() +
                                                "/gpxsamples",
                                                filetypes=fileTypes)
        if len(filename) == 0:
            return
        filename.removesuffix(".gpx")
        filename += ".gpx"
        self.saveFileCallback(filename)

    def addTimeUI(self, column: int, default: str,
                  label: str) -> tuple[customtkinter.CTkTextbox, int]:
        textbox = customtkinter.CTkTextbox(master=self,
                                           corner_radius=0,
                                           height=Config.DEFAULT_HEIGHT,
                                           width=30)
        textbox.grid(row=0,
                     column=column,
                     padx=Config.DEFAULT_PADX_MIDDLE,
                     pady=Config.DEFAULT_PADY)
        textbox.insert((0.0), default)

        label = customtkinter.CTkLabel(master=self,
                                       text=label,
                                       fg_color="transparent")
        label.grid(row=0,
                   column=column + 1,
                   padx=(0, Config.DEFAULT_PADX),
                   pady=Config.DEFAULT_PADY)

        return textbox, column + 2

    def enableApply(self, enable: bool):
        self.btnApply.configure(state="normal" if enable else "disabled")
        self.textboxHours.configure(state="normal" if enable else "disabled")
        self.textboxMinutes.configure(state="normal" if enable else "disabled")
        self.textboxSeconds.configure(state="normal" if enable else "disabled")

    def enableSave(self, enable: bool):
        self.btnSave.configure(state="normal" if enable else "disabled")
