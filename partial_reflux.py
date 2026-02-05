import numpy as np

class PartialReflux:
    def __init__(self, alpha, q, ratio, z_F, x_D, x_W):
        self.alpha = alpha
        self.q = q
        self.ratio = ratio
        self.z_F = z_F
        self.x_D = x_D
        self.x_W = x_W
        self.calculate_operating_line_of_stripping_section()

    def equilibrium_line(self, x):
        y = self.alpha * x / (1 + (self.alpha - 1) * x)
        return y

    def q_line(self, x):
        if self.q != 1:
            y = (self.q / (self.q - 1)) * x - (self.z_F / (self.q - 1))
        else:
            y = x
        return y

    def operating_line_of_rectification_section(self, x):
        y = (self.ratio / (self.ratio + 1)) * x + (self.x_D / (self.ratio + 1))
        return y
    
    def calculate_operating_line_of_stripping_section(self):
        if self.q != 1:
            a1, b1, c1 = self.q / (self.q - 1), -1, self.z_F / (self.q - 1)
        else:
            a1, b1, c1 = 1, 0, self.z_F

        a2, b2, c2 = self.ratio / (self.ratio + 1), -1, -(self.x_D / (self.ratio + 1))

        matrix_A = np.array([[a1, b1],
                             [a2, b2]])
                                    
        matrix_B = np.array([c1, c2])

        try:
            self.intersection = np.linalg.solve(matrix_A, matrix_B)
               
        except np.linalg.LinAlgError:
            print("直线平行或重合，没有唯一交点。")

    def operating_line_of_stripping_section(self, x):    
        slope = (self.intersection[1] - self.x_W) / (self.intersection[0] - self.x_W)    
        y = slope * x - slope * self.x_W + self.x_W
        return y
    
    def equilibrium_line_inverse(self, y):
        x = (-y) / (y * self.alpha - y - self.alpha)
        return x
    
    def calculate_theory_plate(self):
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

        
        
        
        



    

    
