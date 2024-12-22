import customtkinter
from Config import Config
from GUI.ContentFrame import ContentFrame
from GUI.FileFrame import FileFrame
from GUI.MessageBox import MessageBox
from GUI.SettingsFrame import SettingsFrame

from GPXTimeOffset import GPXTimeOffset


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.gpxTimeOffset = GPXTimeOffset()

        self.title(Config.APP_NAME)
        self.moveToCenter()
        self.minsize(Config.APP_MIN_WIDTH, Config.APP_MIN_HEIGHT)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.fileFrame = FileFrame(self, self.openFileCallback)
        self.fileFrame.grid(row=0,
                            column=0,
                            padx=Config.DEFAULT_PADX,
                            pady=Config.DEFAULT_PADY_TOP,
                            sticky="nsew",
                            columnspan=2)

        self.settingsFrame = SettingsFrame(self, self.applySettingsCallback,
                                           self.saveFileCallback)
        self.settingsFrame.grid(row=1,
                                column=0,
                                padx=Config.DEFAULT_PADX,
                                pady=Config.DEFAULT_PADY_TOP,
                                sticky="nsew",
                                columnspan=2)

        self.originalContentFrame = ContentFrame(self, "Original",
                                                 "Select a file")
        self.originalContentFrame.grid(row=2,
                                       column=0,
                                       padx=Config.DEFAULT_PADX,
                                       pady=Config.DEFAULT_PADY_BOTTOM,
                                       sticky="nsew")

        self.modifiedContentFrame = ContentFrame(self, "Modified",
                                                 "Apply an offset")
        self.modifiedContentFrame.grid(row=2,
                                       column=1,
                                       padx=Config.DEFAULT_PADX,
                                       pady=Config.DEFAULT_PADY_BOTTOM,
                                       sticky="nsew")

    def openFileCallback(self, filePath: str):
        try:
            self.originalContentFrame.showContent(
                self.gpxTimeOffset.readFile(filePath))
        except Exception as error:
            MessageBox(parent=self, message=str(error))
        self.settingsFrame.enableApply(True)
        self.settingsFrame.enableSave(False)
        self.modifiedContentFrame.reset()

    def applySettingsCallback(self, offsetHours: int, offsetMinutes: int,
                              offsetSeconds: int):
        try:
            self.modifiedContentFrame.showContent(
                self.gpxTimeOffset.offsetTime(offsetHours=offsetHours,
                                              offsetMinutes=offsetMinutes,
                                              offsetSeconds=offsetSeconds))
        except Exception as error:
            MessageBox(parent=self, message=str(error))
        self.settingsFrame.enableSave(True)

    def saveFileCallback(self, filePath: str):
        try:
            self.gpxTimeOffset.saveFile(filePath)
        except Exception as error:
            MessageBox(parent=self, message=str(error))

    def moveToCenter(self):
        x = int(self.winfo_screenwidth() / 2) - int(
            Config.APP_DEFAULT_WIDTH / 2)
        y = int(self.winfo_screenheight() * 0.6) - int(
            Config.APP_DEFAULT_HEIGHT / 2)

        self.geometry(
            f"{Config.APP_DEFAULT_WIDTH}x{Config.APP_DEFAULT_HEIGHT}+{x}+{y}")


if __name__ == '__main__':
    app = App()
    app.mainloop()
