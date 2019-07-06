import numpy as np

def exFLD(Ex, Cex, Cexly, Cexlz, Hy, Hz):
    NX, NY, NZ = Ex.shape[:3]
    for k in range(1,NZ-1): 
        for j in range(0,NY-1):
            for i in range(1,NX-1):
                Ex[i][j][k] = Cex[i][j][k] * Ex[i][j][k] \
                            + Cexly[i][j][k] * (Hz[i][j][k] - Hz[i][j-1][k]) \
                            - Cexlz[i][j][k] * (Hy[i][j][k] - Hy[i][j][k-1])

    return Ex


def eyFLD(Ey, Cey, Ceylx, Ceylz, Hz, Hx):
    NX, NY, NZ = Ey.shape[:3]
    for k in range(1,NZ-1): 
        for j in range(0,NY-1):
            for i in range(1,NX-1):
                Ey[i][j][k] = Cey[i][j][k] * Ey[i][j][k] \
                            + Ceylz[i][j][k] * (Hx[i][j][k] - Hx[i][j][k-1]) \
                            - Ceylx[i][j][k] * (Hz[i][j][k] - Hz[i-1][j][k])

    return Ey


def ezFLD(Ez, Cez, Cezlx, Cezly, Hx, Hy):
    NX, NY, NZ = Ez.shape[:3]
    for k in range(0,NZ-1): 
        for j in range(1,NY-1):
            for i in range(1,NX-1):
                Ez[i][j][k] = Cez[i][j][k] * Ez[i][j][k] \
                            + Cezlx[i][j][k] * (Hy[i][j][k] - Hy[i-1][j][k]) \
                            - Cezly[i][j][k] * (Hx[i][j][k] - Hx[i][j-1][k])

    return Ez


def hxFLD(Ey, Ez, Chxly, Chxlz, Hx):
    NX, NY, NZ = Hx.shape[:3]
    for k in range(0,NZ-1): 
        for j in range(0,NY-1):
            for i in range(1,NX-1):
                Hx[i][j][k] = Hx[i][j][k] \
                            - Chxly[i][j][k] * (Ez[i][j+1][k] - Ez[i][j][k]) \
                            + Chxlz[i][j][k] * (Ey[i][j][k+1] - Ey[i][j][k])

    return Hx


def hyFLD(Ez, Ex, Chylx, Chylz, Hy):
    NX, NY, NZ = Hy.shape[:3]
    for k in range(0,NZ-1): 
        for j in range(1,NY-1):
            for i in range(0,NX-1):
                Hy[i][j][k] = Hy[i][j][k] \
                            - Chylz[i][j][k] * (Ex[i][j][k+1] - Ex[i][j][k]) \
                            + Chylx[i][j][k] * (Ez[i+1][j][k] - Ez[i][j][k])

    return Hy


def hzFLD(Ex, Ey, Chzlx, Chzly, Hz):
    NX, NY, NZ = Hz.shape[:3]
    for k in range(0,NZ-1): 
        for j in range(0,NY-1):
            for i in range(0,NX-1):
                Hz[i][j][k] = Hz[i][j][k] \
                            - Chzlx[i][j][k] * (Ey[i+1][j][k] - Ey[i][j][k]) \
                            + Chzly[i][j][k] * (Ex[i][j+1][k] - Ex[i][j][k])

    return Hz
