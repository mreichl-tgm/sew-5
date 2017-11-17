"""
:author: Markus Reichl
:version: 19.10.2017
"""


from PySide.QtGui import QMainWindow

from ui.ui import Ui_MainWindow


class View(QMainWindow, Ui_MainWindow):
    """
    Handles the view component of the mvc application
    """
    def __init__(self):
        """
        Instantiates the graphical user interface
        """
        super().__init__()
        self.setupUi(self)
        self.show()
