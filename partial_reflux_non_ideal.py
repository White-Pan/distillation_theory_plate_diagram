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

        if not np.all(np.diff(self.equilibrium_y) > 0):
            raise ValueError("y数据必须严格单调递增以保证反函数存在")

        # 创建 PCHIP 插值器
        self.forward_interp = interpolate.PchipInterpolator(self.equilibrium_x, self.equilibrium_y)
        self.inverse_interp = interpolate.PchipInterpolator(self.equilibrium_y, self.equilibrium_x)

        # 校验 xD / xW 是否越过共沸点（防止 McCabe-Thiele 阶梯发散导致死循环）
        self._validate_composition_range()

        # 校验回流比是否满足最小回流比要求（数值法）
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
        """数值法计算最小回流比 R_min

        q线与平衡线的交点：
        - q != 1：通过检测 q_y - y_eq 差值符号变化来定位交点
        - q == 1：q线为垂直线 x = z_F，直接代入平衡线

        再由 R_min/(R_min+1) = (xD - ye)/(xD - xe) 解出 R_min。

        Returns:
            float: 最小回流比 R_min
        """
        if self.q == 1:
            # q=1 (饱和液体进料): q线为垂直线 x = z_F
            xe = self.z_F
            ye = float(self.forward_interp(xe))
        else:
            q_y = self.q_line(self.equilibrium_x)
            diff = q_y - self.equilibrium_y

            xe = None
            ye = None

            for i in range(1, len(self.equilibrium_x)):
                if diff[i - 1] * diff[i] < 0:
                    # 线性插值精确定位交点
                    t = abs(diff[i - 1]) / (abs(diff[i - 1]) + abs(diff[i]))
                    xe = self.equilibrium_x[i - 1] + t * (self.equilibrium_x[i] - self.equilibrium_x[i - 1])
                    ye = self.equilibrium_y[i - 1] + t * (self.equilibrium_y[i] - self.equilibrium_y[i - 1])
                    break
                elif diff[i] == 0:
                    xe = float(self.equilibrium_x[i])
                    ye = float(self.equilibrium_y[i])
                    break

            if xe is None:
                raise ValueError("q线与平衡线在数据范围内无交点，请检查进料参数与平衡数据。")

        # R_min/(R_min+1) = (xD - ye)/(xD - xe)
        slope = (self.x_D - ye) / (self.x_D - xe)
        R_min = slope / (1 - slope)
        return R_min

    def _validate_composition_range(self):
        """校验 xD / xW 是否在平衡线可正常塔板迭代的范围内

        检测共沸点并确保 xD 和 xW 都在 y > x 的区域（即轻组分为易挥发组分），
        否则 McCabe-Thiele 阶梯会向错误方向发散，导致 calculate_theory_plate 死循环。
        """
        # 1. 检测共沸点（平衡线与对角线相交处，y-x 由正变负）
        azeotrope_x = None
        for i in range(1, len(self.equilibrium_x) - 1):  # 跳过端点 x=0 和 x=1
            d = self.equilibrium_y[i] - self.equilibrium_x[i]
            if d <= 0:
                d_prev = self.equilibrium_y[i - 1] - self.equilibrium_x[i - 1]
                if d < 0:
                    # y-x 在 i-1 和 i 之间变号，线性插值
                    t = abs(d_prev) / (abs(d_prev) + abs(d))
                    azeotrope_x = self.equilibrium_x[i - 1] + t * (self.equilibrium_x[i] - self.equilibrium_x[i - 1])
                else:  # d == 0
                    # 共沸点恰好落在数据点上
                    azeotrope_x = float(self.equilibrium_x[i])
                break

        # 2. 校验 xD：第一步水平阶梯必须向左走（x1 < xD）
        x1_from_top = float(self.equilibrium_line_inverse(self.x_D))
        if x1_from_top >= self.x_D:
            if azeotrope_x is not None and self.x_D > azeotrope_x:
                raise ValueError(
                    f"塔顶组成 xD = {self.x_D:.4f} 越过共沸组成 (x ≈ {azeotrope_x:.4f})。\n"
                    f"共沸点右侧平衡线 y < x，McCabe-Thiele 阶梯将向 x=1 发散导致死循环。\n"
                    f"请将 xD 设置在共沸组成以内（xD < {azeotrope_x:.4f}）。"
                )
            else:
                raise ValueError(
                    f"塔顶组成 xD = {self.x_D:.4f} 不可实现：\n"
                    f"平衡线在 xD 处 y({self.x_D:.4f}) = {float(self.forward_interp(self.x_D)):.4f} < {self.x_D:.4f}，\n"
                    f"McCabe-Thiele 阶梯无法向左收敛。请检查平衡数据或降低 xD。"
                )

        # 3. 校验 xW：第一步竖直阶梯必须向上走（y(xW) > xW）
        y_from_bottom = float(self.forward_interp(self.x_W))
        if y_from_bottom <= self.x_W:
            if azeotrope_x is not None and self.x_W > azeotrope_x:
                raise ValueError(
                    f"塔底组成 xW = {self.x_W:.4f} 越过共沸组成 (x ≈ {azeotrope_x:.4f})。\n"
                    f"共沸点右侧平衡线 y < x，McCabe-Thiele 阶梯将向 x=1 发散。\n"
                    f"请将 xW 设置在共沸组成以内（xW < {azeotrope_x:.4f}）。"
                )
            else:
                raise ValueError(
                    f"塔底组成 xW = {self.x_W:.4f} 不可实现：\n"
                    f"平衡线在 xW 处 y({self.x_W:.4f}) = {y_from_bottom:.4f} <= {self.x_W:.4f}，\n"
                    f"McCabe-Thiele 阶梯无法向上收敛。请检查平衡数据或提高 xW。"
                )

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
