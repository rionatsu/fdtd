import numpy as np

def setup():
    return 0


def output():
    return 0


def eField():
    return 0

def absorbingBC():
    return 0

def hField():
    return 0


if __name__ == "__main__":
    setup()
    timestep = 10
    dt = 0.001
    t = 0

    for i in range(timestep):
        eField()
        absorbingBC()
        t += dt/2
        hField()
        t += dt/2
    
    output()
