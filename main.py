# -*- coding: utf-8 -*-
"""
Author: White Pan
Email: greengiantpanda@outlook.com
Date: 2026.2
Those who are interested can find me at Nanjing Tech University.
"""

import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    

    app.exec()

