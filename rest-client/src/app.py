import sys

from PySide.QtGui import QApplication

from src.control import Control


class App(QApplication):
    def __init__(self):
        """
        Initializes the app and creates an control instance
        """
        super().__init__(sys.argv)
        self.control = Control()

        while self.control.view.isVisible():
            self.control.view.update()
            self.processEvents()

        sys.exit()


if __name__ == '__main__':
    app = App()
    app.exec_()
