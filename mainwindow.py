from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
import partial_reflux
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

    def draw_diagram(self):
        alpha = eval(self.lineEdit_alpha.text())
        ratio = eval(self.lineEdit_ratio.text())
        q = eval(self.lineEdit_q.text())
        z_F = eval(self.lineEdit_z_F.text())
        x_D = eval(self.lineEdit_x_D.text())
        x_W = eval(self.lineEdit_x_W.text())
        process = partial_reflux.DataProcess(alpha, q, ratio, z_F, x_D, x_W)

        x_for_global = np.linspace(0, 1, 50)
        x_for_qline = np.linspace(min([process.intersection[0], z_F]), max([process.intersection[0], z_F]), 50)
        x_for_rectification = np.linspace(0, x_D, 50)
        x_for_stripping = np.linspace(x_W, process.intersection[0], 50)
        
        matplotlib.rcParams['font.family']='Microsoft YaHei'
        matplotlib.rcParams['axes.unicode_minus']=False
        plt.figure(figsize=(8, 8))
        plt.title("精馏塔理论板图")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(0, 1)
        plt.ylim(0, 1)

        plt.plot(x_for_global, x_for_global, label="y = x")
        plt.plot(x_for_global, process.equilibrium_line(x_for_global), label="平衡线")
        plt.plot(x_for_rectification, process.operating_line_of_rectification_section(x_for_rectification),
                                                                                      label="精馏段操作线")
        if q != 1:
            plt.plot(x_for_qline, process.q_line(x_for_qline), label="q线")
        else:
            plt.axvline(x=z_F, ymin=z_F, ymax=process.intersection[1], label="q线")
        plt.plot(x_for_stripping, process.operating_line_of_stripping_section(x_for_stripping),
                                                                                label="提馏段操作线")
        plt.legend()
        

        plate, plate_for_loading = process.calculate_theory_plate()
        print(f"理论板数: {plate}\n加料板: {plate_for_loading}")

        if(True):
            for i in range(len(process.x_list) - 1):
                i_plus_one = i + 1
                plt.axhline(y=process.y_list[i], xmin=process.x_list[i_plus_one], 
                            xmax=process.x_list[i], color="black")
                plt.axvline(x=process.x_list[i_plus_one], ymin=process.y_list[i_plus_one], 
                            ymax=process.y_list[i], color="black")
                
        plt.show()




    
        



