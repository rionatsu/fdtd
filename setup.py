import numpy as np

#########################
# p9 ループ前の初期条件設定#
#########################

#########################
# p34-38 誘電体、磁性体  #
#########################
def setConstraints():
    # 電気定数
    epsilon0 = 8.854e-12
    # 磁気定数
    mu0 = 1.256e-6

    # 0:自遊空間、1:完全導体、2~:誘電体（磁性体）
    epsilon = np.zeros(5)
    sigma = np.zeros(5)
    # mu = np.zeros(5)
    mu = np.full(5,mu0)

    # 自遊空間
    epsilon[0] = epsilon0
    sigma[0] = 0.0

    # 立方体の媒質定数の設定
    epsilon[2] = 5 * epsilon0
    sigma[2] = 0.0

    # 線状誘電体の媒質定数の設定
    epsilon[3] = 10 * epsilon0
    sigma[3] = 5.0

def setFreeSpaceID(IDex, IDey, IDez):
    IDex[:][:][:] = 0
    IDey[:][:][:] = 0
    IDez[:][:][:] = 0

def setCubeID(IDex, IDey, IDez, Xst, Xed, Yst, Yed, Zst, Zed):
    IDex[Xst:Xed][Yst:Yed][Zst:Zed] = 2
    IDey[Xst:Xed][Yst:Yed][Zst:Zed] = 2
    IDez[Xst:Xed][Yst:Yed][Zst:Zed] = 2
    
def setLineID(IDex, IDey, IDez, X0, Y0, Z0, Z1):
    IDez[X0][Y0][Z0:Z1] = 3
    

def setup():

    return 0