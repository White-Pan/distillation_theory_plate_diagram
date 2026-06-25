import numpy as np

class PartialReflux:
    def __init__(self, alpha, q, ratio, z_F, x_D, x_W):
        self.alpha = alpha
        self.q = q
        self.ratio = ratio
        self.z_F = z_F
        self.x_D = x_D
        self.x_W = x_W

        # 校验回流比是否满足最小回流比要求（解析法）
        self.R_min = self.calculate_R_min()
        if self.ratio < self.R_min:
            raise ValueError(
                f"回流比不足！当前 R = {self.ratio:.4f}，"
                f"最小回流比 R_min = {self.R_min:.4f}。\n"
                f"请增大回流比至 R_min 以上"
                f"（工业中通常取 R = {1.1 * self.R_min:.2f} ~ {2.0 * self.R_min:.2f}）。"
            )

        self.calculate_operating_line_of_stripping_section()

    def calculate_R_min(self):
        """解析法计算最小回流比 R_min

        q线与平衡线的交点通过解析求解二次方程得到：
        - q线: y = m*x + b  (q != 1) 或 x = z_F (q == 1)
        - 平衡线: y = alpha*x / (1 + (alpha-1)*x)

        联立得二次方程 A*x^2 + B*x + C = 0，取[0,1]内的根即为 xe。
        再由 R_min/(R_min+1) = (xD - ye)/(xD - xe) 解出 R_min。

        Returns:
            float: 最小回流比 R_min
        """
        if self.q != 1:
            m = self.q / (self.q - 1)
            b = -self.z_F / (self.q - 1)

            # 二次方程系数: A*x^2 + B*x + C = 0
            A = (self.alpha - 1) * m
            B = m + (self.alpha - 1) * b - self.alpha
            C = b

            discriminant = B**2 - 4 * A * C
            if discriminant < 0:
                raise ValueError("q线与平衡线无交点，请检查进料参数。")

            sqrt_disc = np.sqrt(discriminant)
            x1 = (-B + sqrt_disc) / (2 * A)
            x2 = (-B - sqrt_disc) / (2 * A)

            # 选择在 [0, 1] 范围内且离 z_F 最近的根
            xe = None
            for x_candidate in (x1, x2):
                if 0 < x_candidate < 1:
                    if xe is None or abs(x_candidate - self.z_F) < abs(xe - self.z_F):
                        xe = x_candidate

            if xe is None:
                raise ValueError("q线与平衡线在[0,1]范围内无交点，请检查参数。")

            ye = self.equilibrium_line(xe)
        else:
            # q = 1: q线为垂直线 x = z_F
            xe = self.z_F
            ye = self.equilibrium_line(xe)

        # R_min/(R_min+1) = (xD - ye)/(xD - xe)
        slope = (self.x_D - ye) / (self.x_D - xe)
        R_min = slope / (1 - slope)
        return R_min

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
