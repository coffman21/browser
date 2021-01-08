import sys
from player.player import Player
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    p = Player()
    sys.exit(app.exec_())