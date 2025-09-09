import numpy as np
import matplotlib.pyplot as plt
# Packages used ^
# Claire O'Connor & Amelia Abruscato
# Polonius the Projectile Cow Simulator Python Program
    
# Debugging
msg_lvl = 2
def msg(lvl, msg):
    if lvl<msg_lvl:
        print(msg)

def write_pos(time_arr, position_arr):
    f = open("position.out", "w")
    i=0
    for time in time_arr:
        f.write(f"{time} {position_arr[i][0]} {position_arr[i][1]} \n")
        i=i+1
    

def main():

    # Config
    DisplayWithOffset = True # If set to True displays Energy graph with offset vertical axis
    UserInput = False ### possibly add user input option for more convienent experimentation

    # User Inputs
    mass = 1000
    yo = 80
    Cd = 0  # drag constant
    del_t = 0.0001  # time step
    vox = 5
    voy = 6

    # Initial conditions and constants
    g = 9.81
    xo = 0
    time = 0
    Fg = -mass * g

    # Vectors
    pos = np.array([xo, yo])
    vel = np.array([vox, voy])

    # Functions
    def total_force(vel=vel, Fg=Fg):
        Fd = np.array([-Cd * vel[0] * np.absolute(vel[0]), -Cd * vel[1] * np.absolute(vel[1])])
        F = np.array([Fd[0], Fg + Fd[1]])
        return F

    def moment_later(Force, position=pos, velocity=vel, delta_t=del_t):
        a = np.array([F[0]/mass,F[1]/mass])
        post = np.array([pos[0] + vel[0] * del_t, pos[1] + vel[1] * del_t])
        velt = np.array([vel[0] + a[0] * del_t, vel[1] + a[1] * del_t])
        
        return post, velt

    def energy(pos, vel):
        KE = 0.5 * mass * (vel[0]**2 + vel[1]**2)
        PE = mass * g * pos[1]
        E = KE + PE
        return KE, PE, E

    # DATA COLLECTION LISTS
    POSITION = []
    VELOCITY = []
    TIME = []
    ENERGY = []
    position_arr = []

    while pos[1] > 0:

        # Calculating force, position, velocity, and energy of Polonius @ an instant
        F = total_force()
        pos, vel = moment_later(F)
        KE, PE, E = energy(pos, vel)

        # STORING DATA
        
        POSITION.append(np.linalg.norm(pos))
        position_arr.append(pos)
        VELOCITY.append(np.linalg.norm(vel))
        TIME.append(time)
        ENERGY.append(E)

        time += del_t

        msg(5, f"Time: {time:.4f}, Position: {pos}, Velocity: {vel}, KE: {KE:.2f}, PE: {PE:.2f}, Total Energy: {E:.2f}")
    
    write_pos(TIME, position_arr)
    
    Position = np.array(POSITION)
    Velocity = np.array(VELOCITY)
    Time = np.array(TIME)
    Energy = np.array(ENERGY)
    
    # PLOTTING DATA
    '''plt.figure(figsize=(12, 10))

    # Position vs Time
    plt.subplot(3, 1, 1)
    plt.plot(Time, Position, label='Position', color='blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Position vs Time')
    plt.legend()

    # Velocity vs Time
    plt.subplot(3, 1, 2)
    plt.plot(Time, Velocity, label='Velocity', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.legend()

    # Energy vs Time
    plt.subplot(3, 1, 3)
    plt.plot(Time, Energy, label='Total Energy', color='green')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.title('Energy vs Time')
    plt.ticklabel_format(style='plain', axis='y', useOffset=False) #scilimits=(-3, 3))
    plt.legend()
    if DisplayWithOffset:{plt.ylim(0, 900000)}
    plt.ticklabel_format(style='sci', axis='y', useOffset=DisplayWithOffset) #scilimits=(-3, 3))
    plt.tight_layout()

    #plt.show()
    plt.savefig('cow_simulation_plot1.png', dpi=300)'''

    # Plotting y vs x position using time step + analytical solution
    plt.plot(position_arr[1], position_arr[0], label="y vs x Position", color="black")
    plt.xlabel('x Position (m)')
    plt.ylabel('y Position (m)')
    plt.title('y vs x Position')
    plt.legend()

    plt.savefig("yvx.png", dpi=300)

if __name__ == "__main__":
    main()

