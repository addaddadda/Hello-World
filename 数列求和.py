# 引入分数类
from fractions import Fraction


def sum_of_series():
    # 初始化序列和
    s = 0
    # 遍历范围为1到99
    for n in range(1, 100):
        # 添加序列中的值
        s += Fraction(1, (2 * n + 1) * (2 * n - 1))
        # 如果序列和等于99/199则返回遍历数
        if s == Fraction(99, 199):
            return n


if __name__ == '__main__':
    # 调用sum_of_series函数
    print(sum_of_series())
