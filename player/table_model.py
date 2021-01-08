from player.data import track
from player.data.track import Track
from player.orm import ORM
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.orm = ORM("d:\\workspace\\temp")
        self.orm.addTrack(Track("Scary monsters", "Skrill", 5))
        tracks = self.orm.getTracks()
        self.rows = tracks
        self.headers = list(dict(tracks[0]).keys()) if tracks else []

    def rowCount(self, parent):
        return len(self.rows)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        return self.rows[index.row()][self.headers[index.column()]]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return self.headers[section]
