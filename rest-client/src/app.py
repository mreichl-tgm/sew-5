import sys

from PySide import QtGui

from src.control.control import Control


class App(QtGui.QApplication):
    def __init__(self, response_type):
        """
        Initializes the app and creates an control instance
        """
        super().__init__()
        self.control = Control(response_type)

        while self.control.view.isVisible():
            self.control.view.update()
            self.processEvents()

        sys.exit()


if __name__ == '__main__':
    response_type = sys.argv[1]

    app = App(response_type)
    app.exec_()
