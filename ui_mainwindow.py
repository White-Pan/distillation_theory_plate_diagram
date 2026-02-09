# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(593, 493)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_data = QGroupBox(self.centralwidget)
        self.groupBox_data.setObjectName(u"groupBox_data")
        self.groupBox_data.setGeometry(QRect(30, 10, 511, 221))
        self.groupBox_equilibrium = QGroupBox(self.groupBox_data)
        self.groupBox_equilibrium.setObjectName(u"groupBox_equilibrium")
        self.groupBox_equilibrium.setGeometry(QRect(20, 20, 471, 131))
        self.line = QFrame(self.groupBox_equilibrium)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(229, 10, 31, 121))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.radioButton_ideal = QRadioButton(self.groupBox_equilibrium)
        self.radioButton_ideal.setObjectName(u"radioButton_ideal")
        self.radioButton_ideal.setGeometry(QRect(40, 20, 98, 20))
        self.radioButton_ideal.setChecked(True)
        self.label_7 = QLabel(self.groupBox_equilibrium)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 50, 181, 16))
        self.radioButton_non_ideal = QRadioButton(self.groupBox_equilibrium)
        self.radioButton_non_ideal.setObjectName(u"radioButton_non_ideal")
        self.radioButton_non_ideal.setGeometry(QRect(280, 20, 98, 20))
        self.radioButton_non_ideal.setChecked(False)
        self.pushButton_import = QPushButton(self.groupBox_equilibrium)
        self.pushButton_import.setObjectName(u"pushButton_import")
        self.pushButton_import.setGeometry(QRect(280, 70, 151, 24))
        self.label_8 = QLabel(self.groupBox_equilibrium)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 50, 171, 16))
        self.pushButton_help = QPushButton(self.groupBox_equilibrium)
        self.pushButton_help.setObjectName(u"pushButton_help")
        self.pushButton_help.setGeometry(QRect(280, 100, 151, 24))
        self.widget = QWidget(self.groupBox_equilibrium)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(51, 81, 131, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_alpha = QLineEdit(self.widget)
        self.lineEdit_alpha.setObjectName(u"lineEdit_alpha")

        self.horizontalLayout.addWidget(self.lineEdit_alpha)

        self.widget1 = QWidget(self.groupBox_data)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 160, 291, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_q = QLineEdit(self.widget1)
        self.lineEdit_q.setObjectName(u"lineEdit_q")

        self.horizontalLayout_4.addWidget(self.lineEdit_q)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_ratio = QLineEdit(self.widget1)
        self.lineEdit_ratio.setObjectName(u"lineEdit_ratio")

        self.horizontalLayout_4.addWidget(self.lineEdit_ratio)

        self.widget2 = QWidget(self.groupBox_data)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(41, 191, 441, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_z_F = QLineEdit(self.widget2)
        self.lineEdit_z_F.setObjectName(u"lineEdit_z_F")

        self.horizontalLayout_2.addWidget(self.lineEdit_z_F)

        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit_x_D = QLineEdit(self.widget2)
        self.lineEdit_x_D.setObjectName(u"lineEdit_x_D")

        self.horizontalLayout_2.addWidget(self.lineEdit_x_D)

        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lineEdit_x_W = QLineEdit(self.widget2)
        self.lineEdit_x_W.setObjectName(u"lineEdit_x_W")

        self.horizontalLayout_2.addWidget(self.lineEdit_x_W)

        self.groupBox_option = QGroupBox(self.centralwidget)
        self.groupBox_option.setObjectName(u"groupBox_option")
        self.groupBox_option.setGeometry(QRect(30, 240, 231, 51))
        self.radioButton_full = QRadioButton(self.groupBox_option)
        self.radioButton_full.setObjectName(u"radioButton_full")
        self.radioButton_full.setGeometry(QRect(40, 20, 71, 20))
        self.radioButton_full.setChecked(False)
        self.radioButton_full.setAutoRepeat(False)
        self.radioButton_partial = QRadioButton(self.groupBox_option)
        self.radioButton_partial.setObjectName(u"radioButton_partial")
        self.radioButton_partial.setGeometry(QRect(130, 20, 91, 20))
        self.radioButton_partial.setChecked(True)
        self.groupBox_output = QGroupBox(self.centralwidget)
        self.groupBox_output.setObjectName(u"groupBox_output")
        self.groupBox_output.setGeometry(QRect(30, 300, 511, 131))
        self.textBrowser_output = QTextBrowser(self.groupBox_output)
        self.textBrowser_output.setObjectName(u"textBrowser_output")
        self.textBrowser_output.setGeometry(QRect(10, 20, 481, 91))
        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(301, 258, 211, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_draw = QPushButton(self.widget3)
        self.pushButton_draw.setObjectName(u"pushButton_draw")

        self.horizontalLayout_3.addWidget(self.pushButton_draw)

        self.pushButton_quit = QPushButton(self.widget3)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout_3.addWidget(self.pushButton_quit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 593, 33))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox_data.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8f93\u5165", None))
        self.groupBox_equilibrium.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7406\u60f3/\u975e\u7406\u60f3\u7269\u7cfb", None))
        self.radioButton_ideal.setText(QCoreApplication.translate("MainWindow", u"\u7406\u60f3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"y =\u03b1x/(1+(\u03b1-1)x)  \u8f93\u5165\u03b1\u4ee5\u7ee7\u7eed", None))
        self.radioButton_non_ideal.setText(QCoreApplication.translate("MainWindow", u"\u975e\u7406\u60f3", None))
        self.pushButton_import.setText(QCoreApplication.translate("MainWindow", u"\u4ece.csv/.xlsx\u6587\u4ef6\u5bfc\u5165...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165x-y\u7684\u76f8\u5e73\u8861\u6570\u636e\u4ee5\u7ee7\u7eed", None))
        self.pushButton_help.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5bfc\u5165\u987b\u77e5...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u03b1=", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"q=", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"R=", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"z_F=", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"x_D=", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"x_W=", None))
        self.groupBox_option.setTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u9009\u9879", None))
        self.radioButton_full.setText(QCoreApplication.translate("MainWindow", u"\u5168\u56de\u6d41", None))
        self.radioButton_partial.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u5206\u56de\u6d41", None))
        self.groupBox_output.setTitle(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\u680f", None))
        self.pushButton_draw.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u5e76\u4f5c\u56fe", None))
        self.pushButton_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

