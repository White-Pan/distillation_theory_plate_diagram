# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(468, 280)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_draw = QPushButton(self.centralwidget)
        self.pushButton_draw.setObjectName(u"pushButton_draw")
        self.pushButton_draw.setGeometry(QRect(320, 140, 75, 24))
        self.pushButton_quit = QPushButton(self.centralwidget)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setGeometry(QRect(320, 170, 75, 24))
        self.groupBox_data = QGroupBox(self.centralwidget)
        self.groupBox_data.setObjectName(u"groupBox_data")
        self.groupBox_data.setGeometry(QRect(20, 20, 411, 91))
        self.layoutWidget = QWidget(self.groupBox_data)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 381, 52))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_alpha = QLineEdit(self.layoutWidget)
        self.lineEdit_alpha.setObjectName(u"lineEdit_alpha")

        self.horizontalLayout.addWidget(self.lineEdit_alpha)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_q = QLineEdit(self.layoutWidget)
        self.lineEdit_q.setObjectName(u"lineEdit_q")

        self.horizontalLayout.addWidget(self.lineEdit_q)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_ratio = QLineEdit(self.layoutWidget)
        self.lineEdit_ratio.setObjectName(u"lineEdit_ratio")

        self.horizontalLayout.addWidget(self.lineEdit_ratio)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_z_F = QLineEdit(self.layoutWidget)
        self.lineEdit_z_F.setObjectName(u"lineEdit_z_F")

        self.horizontalLayout_2.addWidget(self.lineEdit_z_F)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit_x_D = QLineEdit(self.layoutWidget)
        self.lineEdit_x_D.setObjectName(u"lineEdit_x_D")

        self.horizontalLayout_2.addWidget(self.lineEdit_x_D)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lineEdit_x_W = QLineEdit(self.layoutWidget)
        self.lineEdit_x_W.setObjectName(u"lineEdit_x_W")

        self.horizontalLayout_2.addWidget(self.lineEdit_x_W)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox_option = QGroupBox(self.centralwidget)
        self.groupBox_option.setObjectName(u"groupBox_option")
        self.groupBox_option.setGeometry(QRect(20, 120, 161, 80))
        self.radioButton_no_drawing = QRadioButton(self.groupBox_option)
        self.radioButton_no_drawing.setObjectName(u"radioButton_no_drawing")
        self.radioButton_no_drawing.setGeometry(QRect(30, 20, 98, 20))
        self.radioButton_no_drawing.setChecked(False)
        self.radioButton_no_drawing.setAutoRepeat(False)
        self.radioButton_drawing = QRadioButton(self.groupBox_option)
        self.radioButton_drawing.setObjectName(u"radioButton_drawing")
        self.radioButton_drawing.setGeometry(QRect(30, 50, 98, 20))
        self.radioButton_drawing.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 468, 33))
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
        self.pushButton_draw.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u56fe", None))
        self.pushButton_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.groupBox_data.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8f93\u5165", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u03b1=", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"q=", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"R=", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"z_F=", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"x_D=", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"x_W=", None))
        self.groupBox_option.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u9009\u9879", None))
        self.radioButton_no_drawing.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4f5c\u51fa\u5854\u677f", None))
        self.radioButton_drawing.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u51fa\u5854\u677f", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

