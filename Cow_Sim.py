import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Packages used ^
# Claire O'Connor & Amelia Abruscato
# Polonius the Projectile Cow Simulator Python Program

def main(): # main function
    print("main")

# INITIAL CONDITIONS AND CONSTANTS
mass = 1000
a_g = 9.81

h = 80
pos = np.array([0, h])

vel_ox = 4
vel_oy = 3
vel = np.array([vel_ox, vel_oy])

C_d = 1

time = 0
del_t = 0.1


