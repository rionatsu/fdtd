import numpy as np
#########################
# p10-15 2次元TM_FDTD法 #
#########################

def ezFLD(Ez, Cez, Cezlx, Cezly, Hx, Hy):
    NX, NY = Ez.shape[:2]
    for j in range(1,NY-1):
        for i in range(1,NX-1):
            Ez[i][j] = Cez[i][j] * Ez[i][j] \
                        + Cezlx[i][j] * (Hy[i][j] - Hy[i-1][j]) \
                        - Cezly[i][j] * (Hx[i][j] - Hx[i][j-1])

    return Ez


def hxFLD(Ez, Chxly, Hx):
    NX, NY = Ez.shape[:2]
    for j in range(0,NY-1):
        for i in range(1,NX-1):
            Hx[i][j] = Hx[i][j] \
                        - Chxly[i][j] * (Ez[i][j+1] - Ez[i][j])

    return Hx


def hyFLD(Ez, Chylx, Hy):
    NX, NY = Ez.shape[:2]
    for j in range(1,NY-1):
        for i in range(0,NX-1):
            Hy[i][j] = Hy[i][j] \
                        - Chylx[i][j] * (Ez[i+1][j] - Ez[i][j])

    return Hy

