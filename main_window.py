# Filename: main_window.py
# Main Window-Style application

##############################################################################

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar

##############################################################################

class Window(QMainWindow):
    # Main Window
    def __init__(self, parent=None):
        # Initializer
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel(f"I'm the Main Bitch, Bitch"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu('&Menu')
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm floating in Status Bar Space")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

