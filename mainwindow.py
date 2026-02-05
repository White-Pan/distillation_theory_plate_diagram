from PySide6.QtWidgets import QMainWindow, QStatusBar, QMessageBox
from PySide6.QtCore import QDateTime
from ui_mainwindow import Ui_MainWindow

import partial_reflux
import full_reflux
import data_check

import matplotlib.pyplot as plt 
import matplotlib
import numpy as np

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.setWindowTitle("精馏理论塔板")

        self.pushButton_draw.clicked.connect(self.draw_diagram)
        self.pushButton_quit.clicked.connect(self.app.quit)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)       
        self.checker_partial = data_check.DataCheck([self.lineEdit_alpha,
                                             self.lineEdit_q,
                                             self.lineEdit_ratio,
                                             self.lineEdit_z_F,
                                             self.lineEdit_x_D,
                                             self.lineEdit_x_W])
        self.checker_full = data_check.DataCheck([self.lineEdit_alpha,
                                             self.lineEdit_x_D,
                                             self.lineEdit_x_W])
        self.connect_signal()
        self.update_statusBar()
        self.update_lineEdit()

    def connect_signal(self):
        """连接所有信号槽"""
        self.radioButton_full.toggled.connect(self.update_lineEdit)
        self.radioButton_full.toggled.connect(self.update_statusBar)
        self.radioButton_partial.toggled.connect(self.update_lineEdit)
        self.radioButton_partial.toggled.connect(self.update_statusBar)
        self.actionAbout.triggered.connect(self.show_about_message)
        self.actionHelp.triggered.connect(self.show_help_message)
        for line_edit in self.checker_partial.line_edits:
            if line_edit:
                line_edit.textChanged.connect(self.update_statusBar)
        for line_edit in self.checker_full.line_edits:
            if line_edit:
                line_edit.textChanged.connect(self.update_statusBar)

    def update_statusBar(self):
        """更新状态栏显示"""
        if self.radioButton_partial.isChecked():
            if self.checker_partial.is_all_filled():
                self.statusBar.showMessage(f"部分回流模式：输入完成", 0)
                # 设置为成功样式
                self.statusBar.setStyleSheet("""
                    QStatusBar {
                        background-color: #e8f5e8;
                        color: #2d662d;
                        border-top: 1px solid #b2d8b2;
                        padding: 3px;
                    }
                """)
            else:
                self.statusBar.showMessage(f"部分回流模式：输入未完成", 0)
                # 设置为警告样式
                self.statusBar.setStyleSheet("""
                    QStatusBar {
                        background-color: #fff8e1;
                        color: #8a6d3b;
                        border-top: 1px solid #f0d399;
                        padding: 3px;
                    }
                """)

        else:
            if self.checker_full.is_all_filled():
                self.statusBar.showMessage(f"全回流模式：输入完成", 0)
                # 设置为成功样式
                self.statusBar.setStyleSheet("""
                    QStatusBar {
                        background-color: #e8f5e8;
                        color: #2d662d;
                        border-top: 1px solid #b2d8b2;
                        padding: 3px;
                    }
                """)
            else:
                self.statusBar.showMessage(f"全回流模式：输入未完成", 0)
                # 设置为警告样式
                self.statusBar.setStyleSheet("""
                    QStatusBar {
                        background-color: #fff8e1;
                        color: #8a6d3b;
                        border-top: 1px solid #f0d399;
                        padding: 3px;
                    }
                """)

    def update_lineEdit(self):
        """更新QLineEdit启用状态"""
        if self.radioButton_full.isChecked():
            self.lineEdit_q.setEnabled(False)
            self.lineEdit_ratio.setEnabled(False)
            self.lineEdit_z_F.setEnabled(False)
            self.lineEdit_q.clear()
            self.lineEdit_ratio.clear()
            self.lineEdit_z_F.clear()
            self.lineEdit_q.setPlaceholderText("无需输入")
            self.lineEdit_ratio.setPlaceholderText("无需输入")
            self.lineEdit_z_F.setPlaceholderText("无需输入")

        else:
            self.lineEdit_q.setEnabled(True)
            self.lineEdit_ratio.setEnabled(True)
            self.lineEdit_z_F.setEnabled(True)
            self.lineEdit_q.setPlaceholderText("")
            self.lineEdit_ratio.setPlaceholderText("")
            self.lineEdit_z_F.setPlaceholderText("")

    def show_about_message(self):
        """显示关于信息框"""
        QMessageBox.information(
            self,
            "关于",
            "作者: White Pan\n"
            "Email: greengiantpanda@outlook.com\n"
            "Version: 1.0",
            QMessageBox.StandardButton.Ok
        )

    def show_help_message(self):
        """显示帮助信息框"""
        QMessageBox.information(
            self,
            "帮助",
            "部分回流输入平衡线参数α、进料热状态q、实际回流比R、\n"
            "轻组分进料摩尔组成z_F、轻组分塔顶摩尔组成x_D、轻组分塔底摩尔组成x_W\n\n"
            "部分回流输入平衡线参数α、轻组分塔顶摩尔组成x_D、轻组分塔底摩尔组成x_W",
            QMessageBox.StandardButton.Ok
        )


    def draw_diagram(self):
        """根据选择执行不同的方法组合"""
        if self.radioButton_full.isChecked():
            self.draw_diagram_for_full_reflux()
        else:
            self.draw_diagram_for_partial_reflux()
        

    def draw_diagram_for_partial_reflux(self):
        """计算部分回流理论塔板并作图"""
        # 运行该方法时先检查输入是否完整
        if not self.checker_partial.is_all_filled():
            QMessageBox.critical(
                self,
                "错误",
                " 输入未完成，计算已终止。",
                QMessageBox.Ok
            )
            return 
        
        alpha = eval(self.lineEdit_alpha.text())
        ratio = eval(self.lineEdit_ratio.text())
        q = eval(self.lineEdit_q.text())
        z_F = eval(self.lineEdit_z_F.text())
        x_D = eval(self.lineEdit_x_D.text())
        x_W = eval(self.lineEdit_x_W.text())
        partial_reflux_process = partial_reflux.PartialReflux(alpha, q, ratio, z_F, x_D, x_W)

        x_for_global = np.linspace(0, 1, 50)
        x_for_qline = np.linspace(min([partial_reflux_process.intersection[0], z_F]), max([partial_reflux_process.intersection[0], z_F]), 50)
        x_for_rectification = np.linspace(0, x_D, 50)
        x_for_stripping = np.linspace(x_W, partial_reflux_process.intersection[0], 50)
        
        matplotlib.rcParams['font.family']='Microsoft YaHei'
        matplotlib.rcParams['axes.unicode_minus']=False
        plt.figure(figsize=(8, 8))
        plt.title("精馏塔理论板图(部分回流)")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(0, 1)
        plt.ylim(0, 1)

        plt.plot(x_for_global, x_for_global, label="y = x")
        plt.plot(x_for_global, partial_reflux_process.equilibrium_line(x_for_global), label="平衡线")
        plt.plot(x_for_rectification, partial_reflux_process.operating_line_of_rectification_section(x_for_rectification),
                                                                                      label="精馏段操作线")
        if q != 1:
            plt.plot(x_for_qline, partial_reflux_process.q_line(x_for_qline), label="q线")
        else:
            plt.axvline(x=z_F, ymin=z_F, ymax=partial_reflux_process.intersection[1], label="q线")
        plt.plot(x_for_stripping, partial_reflux_process.operating_line_of_stripping_section(x_for_stripping),
                                                                                label="提馏段操作线")
        plt.legend()
        

        plate, plate_for_loading = partial_reflux_process.calculate_theory_plate()
        print(f"理论板数: {plate}\n加料板: {plate_for_loading}")

        if(True):
            for i in range(len(partial_reflux_process.x_list) - 1):
                i_plus_one = i + 1
                plt.axhline(y=partial_reflux_process.y_list[i], xmin=partial_reflux_process.x_list[i_plus_one], 
                            xmax=partial_reflux_process.x_list[i], color="black")
                plt.axvline(x=partial_reflux_process.x_list[i_plus_one], ymin=partial_reflux_process.y_list[i_plus_one], 
                            ymax=partial_reflux_process.y_list[i], color="black")
                
        plt.show()

        # 在程序中显示结果
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        plain_content = (f"======== {current_time} 部分回流结果========\n" 
                        f"最优加料板: {plate_for_loading}\n" 
                        f"理论板数: {round(plate, 2)}")
        self.textBrowser_output.append(plain_content)


    def draw_diagram_for_full_reflux(self):
        """计算全回流理论塔板并作图"""
        # 运行该方法时先检查输入是否完整
        if not self.checker_full.is_all_filled():
            QMessageBox.critical(
                self,
                "错误",
                " 输入未完成，计算已终止。",
                QMessageBox.Ok
            )
            return
        
        alpha = eval(self.lineEdit_alpha.text())
        x_D = eval(self.lineEdit_x_D.text())
        x_W = eval(self.lineEdit_x_W.text())
        full_reflux_process = full_reflux.FullReflux(alpha, x_D, x_W)

        x_for_global = np.linspace(0, 1, 50)

        matplotlib.rcParams['font.family']='Microsoft YaHei'
        matplotlib.rcParams['axes.unicode_minus']=False
        plt.figure(figsize=(8, 8))
        plt.title("精馏塔理论板图(全回流)")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(0, 1)
        plt.ylim(0, 1)

        plt.plot(x_for_global, x_for_global, label="y = x")
        plt.plot(x_for_global, full_reflux_process.equilibrium_line(x_for_global), label="平衡线")
        plt.legend()

        plate = full_reflux_process.calculate_theory_plate()
        print(f"理论板数: {plate}")


        for i in range(len(full_reflux_process.x_list) - 1):
            i_plus_one = i + 1
            plt.axhline(y=full_reflux_process.y_list[i], xmin=full_reflux_process.x_list[i_plus_one],
                         xmax=full_reflux_process.x_list[i], color="black")
            plt.axvline(x=full_reflux_process.x_list[i_plus_one], ymin=full_reflux_process.y_list[i_plus_one],
                        ymax=full_reflux_process.y_list[i], color="black")
            
        plt.show()

        # 在程序中显示结果
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        plain_content = (f"======== {current_time} 全回流结果========\n" 
                        f"理论板数: {round(plate, 2)}")
        self.textBrowser_output.append(plain_content)


        




    
        



