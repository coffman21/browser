from player.file_manager import FileManager
from config_provider import ConfigProvider
from player.table_model import TableModel
from PyQt5.QtWidgets import *


class Player(QMainWindow):
    def __init__(self, parent=None):
        super().__init__() 
        
        self.setCentralWidget(self.initMainWidget())
        self.setMinimumSize(600,400)
        self.setWindowTitle("Browser")
        self.show()

    def initMainWidget(self):
        
        # table settings go
        tableHeaderView = QHeaderView(0x1)
        tableHeaderView.setCascadingSectionResizes(True)
        tableView = QTableView(tableHeaderView)
        tableView.horizontalHeader().setStretchLastSection(True)

        model = TableModel(ConfigProvider.getDbPath())
        tableView.setModel(model)

        button = QPushButton('click')
        button.clicked.connect(self.onButtonClicked)

        topLayout = QVBoxLayout()
        topLayout.addWidget(button)
        topLayout.addWidget(tableView)

        mainWidget = QWidget()
        mainWidget.setLayout(topLayout)

        return mainWidget

    def onButtonClicked(self):
        alert = QMessageBox()
        alert.setText('clicked!')
        alert.exec_()

    
    def main(self):
        pass
