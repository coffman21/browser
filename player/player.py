from player.file_manager import FileManager
from config_provider import ConfigProvider
from player.table_model import TableModel
import sys
from PyQt5.QtWidgets import *


class Player(QMainWindow):
    def __init__(self, parent=None):
        super().__init__() 

        # table settings go
        tableHeaderView = QHeaderView(0x1)
        tableHeaderView.setCascadingSectionResizes(True)
        tableView = QTableView(tableHeaderView)
        tableView.horizontalHeader().setStretchLastSection(True)

        model = TableModel(ConfigProvider.getDbPath())
        tableView.setModel(model)

        topLayout = QVBoxLayout()
        topLayout.addWidget(tableView)

        mainWidget = QWidget()
        mainWidget.setLayout(topLayout)

        self.setCentralWidget(mainWidget)
        self.setMinimumSize(600,400)
        self.setWindowTitle("Browser")
        self.show()

    def main(self):
        pass
