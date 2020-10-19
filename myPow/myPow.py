"""
Author : Qi
Date : 2020/10/19
Link : https://leetcode-cn.com/problems/powx-n/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        使用递归
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n >= 0:
            ret = self.myPow(x, n // 2)
            if n % 2 == 0:  # 偶数
                return ret * ret
            else:
                return ret * ret * x
        else:
            return 1 / self.myPow(x, -n)

    def myPow2(self, x: float, n: int) -> float:
        """
        使用快速幂+迭代
        :param x:
        :param n:
        :return:
        """

        def quickMul(N: int) -> float:
            ans = 1.0
            # 贡献的初始值为 x
            x_temp = x
            # 在对二进制进行拆分的时候记录答案
            while N > 0:
                # 如果N 二进制表示的最低位为1，需要计入贡献
                if N % 2 == 1:
                    ans *= x_temp
                # 将贡献不断平方
                x_temp *= x_temp
                # 舍弃二进制最低位
                N = N // 2
            return ans

        return quickMul(n) if n >= 0 else quickMul(-n)

    def myPow3(self, x: float, n: int) -> float:
        """
        尝试减少迭代次数
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        if n >= 0:
            ret = self.myPow(x, n // 3)
            if n % 3 == 0:
                return ret * ret * ret
            elif n % 3 == 1:
                return ret * ret * ret * x
            else:
                return ret * ret * ret * x * x
        else:
            return 1 / self.myPow(x, -n)


if __name__ == '__main__':
    # 用例
    s = Solution()
    print(s.myPow(2.1, 3), s.myPow2(2.1, 3), s.myPow3(2.1, 3))
    print(s.myPow(0.9, 99999), s.myPow2(0.9, 99999), s.myPow3(0.9, 99999))
    print(s.myPow(2.1, 68), s.myPow2(2.1, 68), s.myPow3(2.1, 68))
