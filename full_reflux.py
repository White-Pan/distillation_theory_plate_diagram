import numpy as np

class FullReflux:
    """全回流类
    
    表示一个全回流过程，支持计算平衡线、平衡线反函数及理论塔板。
    
    Attributes:
        alpha (float): 理想状态下平衡线参数α
        x_D (float): 轻组分塔顶含量
        x_W (float): 轻组分塔底含量
    """
    def __init__(self, alpha, x_D, x_W):
        self.alpha = alpha
        self.x_D = x_D
        self.x_W = x_W

    def equilibrium_line(self, x):
        """平衡线计算

        Args:
            x (float): 液相组分
            
        Returns:
            float: 汽相组分
        """
        y = self.alpha * x / (1 + (self.alpha - 1) * x)
        return y
    
    def equilibrium_line_inverse(self, y):
        """平衡线反函数计算

        Args:
            y (float): 汽相组分
            
        Returns:
            float: 液相组分
        """
        x = (-y) / (y * self.alpha - y - self.alpha)
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