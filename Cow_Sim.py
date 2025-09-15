import numpy as np
import matplotlib.pyplot as plt
# Packages used ^
# Claire O'Connor, Amelia Abruscato & Shreyan Goswami
# Polonius the Projectile Cow Simulator Python Program

# INITIAL CONDITIONS & CONSTANTS
m = 1000
cd = 0       # drag coefficient
xo = 0
yo = 1000
vox = 1
voy = 100
dt = 0.1
g = 9.81

# DEBUGGING
msg_lvl = 2
def msg(level, msg):
    if level < msg_lvl:
        print(msg)

# SIMULATION FUNCTIONS
def analytic_trajectory(x_arr, xo, yo, vox, voy, g):
    # take initial position in two axes (xo and yo), x_arr is the array of x positions, vox is the initial velocity in the x direction, voy same in y direction
    #this is basically y in terms of x (making a quadratic out of it, removing time)
    return yo + (voy / vox) * (x_arr - xo) - (0.5 * g / vox**2) * (x_arr - xo)**2

def calculate_drag_force(velocity):
    #calculating drag force by multiplying velocity with the drag coefficient
    return np.array([-cd * velocity[0] * abs(velocity[0]),
                     -cd * velocity[1] * abs(velocity[1])])

def total_force(velocity):
    #adding the force due to g and drag
    Fd = calculate_drag_force(velocity)
    Fg = -m * g
    return np.array([Fd[0], Fd[1] + Fg])

def moment_later(position, velocity, force, dt):
    #finding the new posotion and velocity 
    acceleration = force / m
    new_pos = position + velocity * dt
    new_vel = velocity + acceleration * dt
    return new_pos, new_vel

def calculate_energy(position, velocity):
    #using standard formulae to find Kinetic and Potential Energy.
    KE = 0.5 * m * np.sum(velocity**2)
    PE = m * g * position[1]
    E = KE + PE
    return KE, PE, E

def write_positions(times, positions, filename="position.out"):
    #entering the positions into position.out file
    with open(filename, "w") as f:
        for t, pos in zip(times, positions):
            f.write(f"{t:.5f} {pos[0]:.5f} {pos[1]:.5f}\n")

def run_simulation():
    position = np.array([xo, yo], dtype=float)
    velocity = np.array([vox, voy], dtype=float)
    time = 0.0

    # STORING DATA
    times, positions, velocities = [], [], []
    kinetic_energy, potential_energy, total_energy = [], [], []

#making a loop to ensure that it runs till position is 0
    while position[1] > 0:
        force = total_force(velocity)
        position, velocity = moment_later(position, velocity, force, dt)
        ke, pe, te = calculate_energy(position, velocity)

        times.append(time)
        positions.append(position.copy())
        velocities.append(np.linalg.norm(velocity))
        kinetic_energy.append(ke)
        potential_energy.append(pe)
        total_energy.append(te)

        time += dt
        msg(5, f"Time: {time:.4f}, Pos: {position}, Vel: {velocity}, KE: {ke:.2f}, PE: {pe:.2f}, E: {te:.2f}")

    return np.array(times), np.array(positions), np.array(kinetic_energy), np.array(potential_energy), np.array(total_energy)

# PLOTTING
def plot_results(times, positions, kinetic, potential, total, xo, yo, vox, voy, g, dt):
    x_vals = positions[:, 0]
    y_vals = positions[:, 1]

    # TRAJECTORY
    fig1, ax1 = plt.subplots(figsize=(8, 6))

    ax1.plot(x_vals, y_vals, label="Numeric", color="blue")

    x_analytic = np.linspace(xo, x_vals[-1], 500)
    y_analytic = analytic_trajectory(x_analytic, xo, yo, vox, voy, g)
    ax1.plot(x_analytic, y_analytic, '--', label="Analytic", color="red")
    #plot specs
    ax1.set_xlabel("x (m)")
    ax1.set_ylabel("y (m)")
    ax1.set_title("y vs x (no drag)")
    ax1.set_ylim(bottom=0)
    ax1.legend()
    ax1.text(
        0.05, 0.95,  # x and y in *axes fraction* (0 to 1)
        f"dt = {dt}",  # Text string
        transform=ax1.transAxes,  # Use axes coordinates
        fontsize=10,
        verticalalignment='top',
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.5)
    )
    ax1.grid()

    plt.tight_layout()
    fig1.savefig(f"trajectory_dt_{dt}.png", dpi=300)
    plt.close(fig1)  # Close figure after saving to avoid overlap

    # ENERGY
    fig2, ax2 = plt.subplots(figsize=(8, 6))

    ax2.plot(times, kinetic, label="Kinetic", color="blue")
    ax2.plot(times, potential, label="Potential", color="orange")
    ax2.plot(times, total, label="Total", color="green")

    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Energy (J)")
    ax2.set_title(f"Energy vs Time")
    ax2.legend()
    ax2.grid()

    plt.tight_layout()
    fig2.savefig("energy.png", dpi=300)
    plt.close(fig2)  # Close figure to free memory

# MAIN FUNCTION
def main():
    times, positions, kinetic, potential, total = run_simulation()
    write_positions(times, positions)
    plot_results(times, positions, kinetic, potential, total, xo, yo, vox, voy, g, dt)

if __name__ == "__main__":
    main()