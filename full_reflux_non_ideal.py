import numpy as np
from scipy import interpolate

class FullRefluxNonIdeal:
    def __init__(self, equilibrium_x, equilibrium_y, x_D, x_W):
        """
        处理部分回流、非理想物系的理论塔板
        
        Args:
            equilibrium_x (list): 液相平衡组成数据列表
            equilibrium_y (list): 汽相平衡组成数据列表
            x_D(float): 轻组分塔顶摩尔分数
            x_W(float): 轻组分塔底摩尔分数
        """
        self.equilibrium_x = np.array(equilibrium_x)
        self.equilibrium_y = np.array(equilibrium_y)
        self.x_D = x_D
        self.x_W = x_W

        if not np.all(np.diff(self.equilibrium_y) > 0):
            raise ValueError("y数据必须严格单调递增以保证反函数存在")
        
        # 创建 PCHIP 插值器
        self.forward_interp = interpolate.PchipInterpolator(self.equilibrium_x, self.equilibrium_y)
        self.inverse_interp = interpolate.PchipInterpolator(self.equilibrium_y, self.equilibrium_x)


    def equilibrium_line(self, x):
        """平衡线, 从x计算y
        
        Args:
            x(ndarray or float): 液相平衡组成

        Returns:
            ndarray or float: 汽相平衡组成
        """
        y = self.forward_interp(x)
        return y  


    def equilibrium_line_inverse(self, y):
        """平衡线, 从y计算x
        
        Args:
            y(ndarray or float): 汽相平衡组成

        Returns:
            ndarray or float: 液相平衡组成
        """
        x = self.inverse_interp(y)
        return x 
    

    def calculate_theory_plate(self):
        """计算全回流理论塔板数

        Returns:
            float: 理论塔板数
        """ 
        plate = 0
        self.x_list = [self.x_D]      
        self.y_list = [self.x_D]

        while(self.x_list[-1] > self.x_W):
            plate += 1
            x_temp = self.equilibrium_line_inverse(self.y_list[-1])
            self.x_list.append(x_temp)
            self.y_list.append(x_temp)

        plate -= (self.x_list[-1] - self.x_W) / (self.x_list[-1] - self.x_list[-2])
        return plate
