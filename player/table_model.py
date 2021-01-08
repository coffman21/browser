from config_provider import ConfigProvider
from player.file_manager import FileManager
from player.data import track
from player.data.track import Track
from player.orm import ORM
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TableModel(QAbstractTableModel):
    def __init__(self, path, parent=None):
        super().__init__(parent)

        self.orm = ORM(path)

        fm = FileManager(ConfigProvider.getLibraryPath())
        tracks = fm.walk()
        self.orm.addTracks(tracks)

        tracks = self.orm.getTracks()
        self.rows = tracks
        self.headers = Track.attributes()

    def rowCount(self, parent):
        return len(self.rows)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        row = self.rows[index.row()]
        return row.get(self.headers[index.column()])

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return self.headers[section]
