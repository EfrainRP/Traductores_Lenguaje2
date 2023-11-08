# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analizadorLexico.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 558)
        icon = QIcon()
        icon.addFile(u"PNG/image.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.lexico = QWidget(MainWindow)
        self.lexico.setObjectName(u"lexico")
        self.pushButton = QPushButton(self.lexico)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 60, 81, 41))
        self.tableTokens = QTableWidget(self.lexico)
        self.tableTokens.setObjectName(u"tableTokens")
        self.tableTokens.setGeometry(QRect(20, 310, 741, 221))
        self.InputText = QTextEdit(self.lexico)
        self.InputText.setObjectName(u"InputText")
        self.InputText.setGeometry(QRect(30, 20, 281, 271))
        self.inputText2 = QTextEdit(self.lexico)
        self.inputText2.setObjectName(u"inputText2")
        self.inputText2.setGeometry(QRect(480, 20, 281, 271))
        MainWindow.setCentralWidget(self.lexico)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
    # retranslateUi

