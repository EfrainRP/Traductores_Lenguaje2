# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(570, 567)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(86, 86, 86, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush2 = QBrush(QColor(255, 170, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"Tarea_6_AnalizadorSintatico\image.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.lexico = QWidget(MainWindow)
        self.lexico.setObjectName(u"lexico")
        self.pushButton = QPushButton(self.lexico)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 10, 81, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.tableTokens = QTableWidget(self.lexico)
        if (self.tableTokens.columnCount() < 3):
            self.tableTokens.setColumnCount(3)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableTokens.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableTokens.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setKerning(True)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setForeground(brush3);
        self.tableTokens.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableTokens.setObjectName(u"tableTokens")
        self.tableTokens.setGeometry(QRect(10, 300, 551, 241))
        font3 = QFont()
        font3.setPointSize(12)
        self.tableTokens.setFont(font3)
        self.tableTokens.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableTokens.setTextElideMode(Qt.ElideNone)
        self.tableTokens.setSortingEnabled(False)
        self.tableTokens.horizontalHeader().setCascadingSectionResizes(False)
        self.tableTokens.horizontalHeader().setMinimumSectionSize(80)
        self.tableTokens.horizontalHeader().setDefaultSectionSize(181)
        self.tableTokens.horizontalHeader().setStretchLastSection(False)
        self.InputText = QTextEdit(self.lexico)
        self.InputText.setObjectName(u"InputText")
        self.InputText.setGeometry(QRect(10, 10, 281, 271))
        self.InputText.setFont(font3)
        self.inputText2 = QTextEdit(self.lexico)
        self.inputText2.setObjectName(u"inputText2")
        self.inputText2.setGeometry(QRect(310, 70, 251, 211))
        font4 = QFont()
        font4.setPointSize(14)
        self.inputText2.setFont(font4)
        self.inputText2.setReadOnly(True)
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
        ___qtablewidgetitem = self.tableTokens.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Lexemas", None));
        ___qtablewidgetitem1 = self.tableTokens.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tokens", None));
        ___qtablewidgetitem2 = self.tableTokens.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
    # retranslateUi

