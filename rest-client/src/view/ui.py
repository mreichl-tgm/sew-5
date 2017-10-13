# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui.ui'
#
# Created: Fri Oct 13 12:35:38 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.form_layout = QtGui.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.label_origin = QtGui.QLabel(self.centralwidget)
        self.label_origin.setObjectName("label_origin")
        self.form_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_origin)
        self.label_target = QtGui.QLabel(self.centralwidget)
        self.label_target.setObjectName("label_target")
        self.form_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_target)
        self.line_origin = QtGui.QLineEdit(self.centralwidget)
        self.line_origin.setObjectName("line_origin")
        self.form_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_origin)
        self.line_target = QtGui.QLineEdit(self.centralwidget)
        self.line_target.setObjectName("line_target")
        self.form_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_target)
        self.verticalLayout_2.addLayout(self.form_layout)
        self.button_show = QtGui.QPushButton(self.centralwidget)
        self.button_show.setObjectName("button_show")
        self.verticalLayout_2.addWidget(self.button_show)
        self.text_browser = QtGui.QTextBrowser(self.centralwidget)
        self.text_browser.setObjectName("text_browser")
        self.verticalLayout_2.addWidget(self.text_browser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "Rest Client", None, QtGui.QApplication.UnicodeUTF8))
        self.label_origin.setText(
            QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_target.setText(
            QtGui.QApplication.translate("MainWindow", "Ziel", None, QtGui.QApplication.UnicodeUTF8))
        self.button_show.setText(
            QtGui.QApplication.translate("MainWindow", "Show me how!", None, QtGui.QApplication.UnicodeUTF8))
