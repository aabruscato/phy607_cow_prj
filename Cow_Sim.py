import numpy as np
import matplotlib.pyplot as plt
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
    delt = 0.0001  # time step
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

    def moment_later(pos, vel, F, del_t):
        a = np.array([F[0]/mass,F[1]/mass])
        post = np.array([pos[0] + vel[0] * delt, pos[1] + vel[1] * delt])
        velt = np.array([vel[0] + a[0] * delt, vel[1] + a[1] * delt])
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

    while pos[1] > 0:

        # Calculating force, position, velocity, and energy of Polonius @ an instant
        F = total_force(vel)
        pos, vel = moment_later(pos, vel, F, delt)
        KE, PE, E = energy(pos, vel)

        # STORING DATA
        POSITION.append(np.linalg.norm(pos))
        VELOCITY.append(np.linalg.norm(vel))
        TIME.append(time)
        ENERGY.append(E)

        time += delt

        print(f"Time: {time:.4f}, Position: {pos}, Velocity: {vel}, KE: {KE:.2f}, PE: {PE:.2f}, Total Energy: {E:.2f}")

    Position = np.array(POSITION)
    Velocity = np.array(VELOCITY)
    Time = np.array(TIME)
    Energy = np.array(ENERGY)

    # PLOTTING DATA
    plt.figure(figsize=(12, 10))

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
    plt.ticklabel_format(style='sci', axis='y', scilimits=(-3, 3))
    plt.legend()

    plt.tight_layout()

    #plt.show()
    plt.savefig('cow_simulation_plot.png', dpi=300)

if __name__ == "__main__":
    main()

