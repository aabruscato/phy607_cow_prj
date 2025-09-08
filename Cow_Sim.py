import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Packages used ^
# Claire O'Connor & Amelia Abruscato
# Polonius the Projectile Cow Simulator Python Program

def main():

    # Initial conditions and constants
    mass = 1000
    g = 9.81
    xo = 0
    time = 0

    # Variables
    h = 80
    Cd = 1  # drag constant
    del_t = 0.0001  # time step
    vox = 5
    voy = 6

    # Vectors
    pos = np.array([xo, h])
    vel = np.array([vox, voy])

    # Functions
    def total_force(vel):
        Fg = np.array([0, -mass * g])
        Fd = np.array([-Cd * vel[0] ** 2, -Cd * vel[1] ** 2])
        F = np.array([Fg[0] + Fd[0], Fg[1] + Fd[1]])
        return F

    #def moment_later(pos, vel, del_t):


    #def energy(pos, vel):






if __name__ == "__main__":
    main()

