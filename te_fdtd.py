import numpy as np

def exFLD(Ex, Cex, Cexly, Hz):
    NX, NY = Ex.shape[:2]
    for j in range(1,NY-1):
        for i in range(0,NX-1):
            Ex[i][j] = Cex[i][j] * Ex[i][j] \
                        + Cexly[i][j] * (Hz[i][j] - Hz[i][j-1])

    return Ex


def eyFLD(Ey, Cey, Ceylx, Hz):
    NX, NY = Ey.shape[:2]
    for j in range(0,NY-1):
        for i in range(1,NX-1):
            Ey[i][j] = Cey[i][j] * Ey[i][j] \
                        + Ceylx[i][j] * (Hz[i][j] - Hz[i-1][j])

    return Ey


def hzFLD(Ex, Ey, Chzlx, Chzly, Hz):
    NX, NY = Hz.shape[:2]
    for j in range(0,NY-1):
        for i in range(0,NX-1):
            Hz[i][j] = Hz[i][j] \
                        - Chzlx[i][j] * (Ey[i+1][j] - Ey[i][j]) \
                        - Chzly[i][j] * (Ex[i][j+1] - Ex[i][j]) 

    return Hz

