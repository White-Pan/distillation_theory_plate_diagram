import numpy as np
from scipy import interpolate

class PartialRefluxNonIdeal:
    def __init__(self, equilibrium_x, equilibrium_y, q, ratio, z_F, x_D, x_W):
        """
        处理部分回流、非理想物系的理论塔板
        
        Args:
            equilibrium_x (list): 液相平衡组成数据列表
            equilibrium_y (list): 汽相平衡组成数据列表
            q(float): 进料热状态
            ratio(float): 实际回流比
            z_F(float): 轻组分进料摩尔分数
            x_D(float): 轻组分塔顶摩尔分数
            x_W(float): 轻组分塔底摩尔分数
        """
        self.equilibrium_x = np.array(equilibrium_x)
        self.equilibrium_y = np.array(equilibrium_y)
        self.q = q
        self.ratio = ratio
        self.z_F = z_F
        self.x_D = x_D
        self.x_W = x_W
        self.calculate_operating_line_of_stripping_section()

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

    def q_line(self, x):
        """q线(或称进料线)

        Args:
            x(ndarray or float): 液相平衡组成

        Returns:
            ndarray or float: 汽相平衡组成
        """
        if self.q != 1:
            y = (self.q / (self.q - 1)) * x - (self.z_F / (self.q - 1))
        else:
            y = x
        return y
    
    def operating_line_of_rectification_section(self, x):
        """精馏段操作线

        Args:
            x(ndarray or float): 液相平衡组成

        Returns:
            ndarray or float: 汽相平衡组成
        """
        y = (self.ratio / (self.ratio + 1)) * x + (self.x_D / (self.ratio + 1))
        return y
    
    def calculate_operating_line_of_stripping_section(self):
        """计算精馏段、q线、提馏段的交点, 建立属性"""
        if self.q != 1:
            a1, b1, c1 = self.q / (self.q - 1), -1, self.z_F / (self.q - 1)
        else:
            a1, b1, c1 = 1, 0, self.z_F

        a2, b2, c2 = self.ratio / (self.ratio + 1), -1, -(self.x_D / (self.ratio + 1))

        matrix_A = np.array([[a1, b1],
                             [a2, b2]])
                                    
        matrix_B = np.array([c1, c2])

        try:
            # 下一行代码计算线性方程组, AX = b, X为解向量 X = (x, y)
            self.intersection = np.linalg.solve(matrix_A, matrix_B)      
        except np.linalg.LinAlgError:
            print("直线平行或重合，没有唯一交点。")


    def operating_line_of_stripping_section(self, x): 
        """提馏段操作线

        Args:
            x(ndarray or float): 液相平衡组成

        Returns:
            ndarray or float: 汽相平衡组成
        """  
        slope = (self.intersection[1] - self.x_W) / (self.intersection[0] - self.x_W)    
        y = slope * x - slope * self.x_W + self.x_W
        return y
    

    def calculate_theory_plate(self):
        """计算塔板以及最佳进料位置

        Returns:
            tuple: (塔板数，最佳进料板)
        """  
        plate = 0
        rectification_section_flag = True
        self.x_list = [self.x_D]
        self.y_list = [self.x_D]

        while(self.x_list[-1] > self.x_W):
            plate += 1
            x_temp = self.equilibrium_line_inverse(self.y_list[-1])
            self.x_list.append(x_temp)            
            if(self.x_list[-1] <= self.intersection[0] and rectification_section_flag):
                rectification_section_flag = False
                plate_for_loading = plate
            if(rectification_section_flag):
                y_temp = self.operating_line_of_rectification_section(self.x_list[-1]) 
            else:
                y_temp = self.operating_line_of_stripping_section(self.x_list[-1])
            self.y_list.append(y_temp) 
            
        # 此步骤为了将最后一个点落在对角线上，注释掉下一行代码对最终结果无影响，但最后一个点会落在提馏线上。
        self.y_list[-1] = self.x_list[-1]

        plate -= (self.x_list[-1] - self.x_W) / (self.x_list[-1] - self.x_list[-2])
        return plate, plate_for_loading
    



 