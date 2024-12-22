import datetime
from copy import copy

from bs4 import BeautifulSoup


class GPXTimeOffset():

    def __init__(self):
        self.xmlData: BeautifulSoup = None
        self.modifiedXMLData: BeautifulSoup = None

    def reset(self):
        self.xmlData = None
        self.modifiedXMLData = None

    def readFile(self, filePath: str) -> str:
        with open(filePath, 'r') as f:
            self.xmlData = BeautifulSoup(f.read(), features="xml")
            return self.xmlData.prettify()
        raise "Unable to open / parse file"

    def offsetTime(self,
                   offsetHours: int,
                   offsetMinutes: int = 0,
                   offsetSeconds: int = 0) -> str:
        if self.xmlData is None:
            raise Exception("Open a file first")

        self.modifiedXMLData = copy(self.xmlData)
        for time in self.modifiedXMLData.find_all("time"):
            timestr = time.text
            rawtime = datetime.datetime.strptime(timestr,
                                                 "%Y-%m-%dT%H:%M:%S.%fZ")
            rawtime += datetime.timedelta(hours=offsetHours,
                                          minutes=offsetMinutes,
                                          seconds=offsetSeconds)
            time.string.replace_with(
                rawtime.strftime("%Y-%m-%dT%H:%M:%S.000Z"))

        return self.modifiedXMLData.prettify()

    def saveFile(self, filePath: str):
        if self.modifiedXMLData is None:
            raise Exception("Nothing to save")
        with open(filePath, 'w') as f:
            f.write(str(self.modifiedXMLData))
