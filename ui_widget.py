# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(491, 261)
        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 491, 261))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u76f8\u5e73\u8861\u6570\u636e\u8868\u683c\u6587\u4ef6\u5236\u4f5c\u8bf4\u660e\uff1a</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u53ef\u5728GitHub\u4e0b\u8f7d\u4e59\u9187-\u6c34\u7269\u7cfb\u7684Excel\u6216CSV\u6587"
                        "\u4ef6\u793a\u4f8b</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/White-Pan/distillation_theory_plate_diagram\"><span style=\" font-size:10pt; text-decoration: underline; color:#258292;\">https://github.com/White-Pan/distillation_theory_plate_diagram</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.  x-y\u5728\u76f8\u5e73\u8861\u6570\u636e\u5728Excel\u4e2d\u5e94\u4e3a2\u5217\uff08x\u6570\u636e\u5728\u7b2cA\u5217\uff0cy\u6570\u636e\u5728\u7b2cB\u5217\u3002</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">     \u884c\u6570\u4efb\u610f\uff0c\u4f46\u6c42\u51c6\u786e\u5e94\u670920\u884c\u4ee5\u4e0a\uff09</span></p>\n"
"<p style=\" margin-top:12px; marg"
                        "in-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.  </span><span style=\" font-size:10pt; font-weight:700;\">\u5fc5\u987b</span><span style=\" font-size:10pt;\">\u5728Excel\u4e2d\u7684\u7b2c\u4e00\u884c\u5199\u4e0a\u5217\u6807\u9898\uff08\u4f8b\u5982\u5728A1\u4e0a\u5199\u2018x\u2019\uff0c\u5728B1\u4e0a\u5199\u2018y\u2019\uff09</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.  \u4e0d\u5141\u8bb8\u6709\u4efb\u4f55\u7f3a\u5931\u7684\u6570\u636e\uff08\u5373x\u7684\u6570\u636e\u4e2a\u6570\u4e0ey\u7684\u6570\u636e\u4e2a\u6570\u76f8\u7b49\uff09</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4.  x-y\u76f8\u5e73\u8861\u6570\u636e</span><span style=\" font-size:10pt; font-weight:700;\">\u5fc5\u987b</sp"
                        "an><span style=\" font-size:10pt;\">\u5305\u542b\u70b9(0, 0)\u4ee5\u53ca\u70b9(1, 1)\uff0c</span><span style=\" font-size:10pt; font-weight:700;\">\u6570\u636e\u987a\u5e8f\u4ece\u5c0f\u5230\u5927</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">*\uff08\u53ef\u9009\uff09\u70b9\u51fbExcel\u7684\u53e6\u5b58\u4e3a\uff0c\u4fdd\u5b58\u4e3aCSV\uff08\u9017\u53f7\u5206\u9694\uff09\u6587\u4ef6</span></p></body></html>", None))
    # retranslateUi

