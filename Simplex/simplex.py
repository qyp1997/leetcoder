import numpy as np
'''
Author:Qi
Date:2020/10/18
'''

def simplex(data, minOrMax=True):
    """
    单纯形法
    :param data:矩阵
    :param minOrMax:True为min函数，False为max函数,默认为计算min函数
    :return:结果
    """
    c = data[0, 0:data.shape[1] - 1]
    A = data[1:]
    c2 = list(range(len(c) - A.shape[0], len(c)))
    while True:
        cb = [c[i] for i in c2]
        r = []
        for i in range(len(c)):
            if minOrMax is True:
                r.append(np.dot(cb, A[..., i]) - c[i])
            else:
                r.append(c[i] - np.dot(cb, A[..., i]))
        if max(r) <= 0:  # r中全部<=0 跳出循环 返回
            break
        inIndex = r.index(max(r))  # A中换入变量序号
        theta = []  # 计算θ
        for i in range(len(c2)):
            if A[i, inIndex] <= 0:
                theta.append(float('inf'))
            else:
                theta.append(A[i, len(c)] / A[i, inIndex])
        if min(theta) is float('inf'):
            break
        outIndex = theta.index(min(theta))  # theta中 换出变量序号
        c2[outIndex] = inIndex  # 修改矩阵c2 改变标准矩阵序列
        # 将inIndex所在列进行初等行变换
        A[outIndex] = A[outIndex] / A[outIndex, inIndex]
        for i in range(len(c2)):
            if i != outIndex:
                A[i] = A[i] - A[outIndex] * A[i, inIndex]
    cb = [c[c2[i]] for i in range(A.shape[0])]
    b = A[..., len(c)]
    return np.dot(cb, b)


# 例子
if __name__ == '__main__':
    # min函数
    data_min = np.loadtxt('data_min.txt', dtype=np.float)
    print('min函数结果为：{}'.format(simplex(data_min, True)))
    # max函数
    data_max = np.loadtxt('data_max.txt', dtype=np.float)
    print('max函数结果为：{}'.format(simplex(data_max, False)))
