"""
    Import useful packages
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

# Constants
G = 6.67430e-11
M_SUN = 1.989e30
AU = 1.496e11
DAY_TIME = 60 * 60 * 24
TOTAL_TIME = 365 * 24 * 60 * 60 * 2
N_STEPS = int(TOTAL_TIME / DAY_TIME)


class CelestialObject:
    def __init__(self, mass, initial_position, initial_velocity, color, name):
        self.mass = mass
        self.position = np.array(initial_position)
        self.velocity = np.array(initial_velocity)
        self.color = color
        self.name = name

    def gravitational_force(self, other_obj_position):
        """
            Compute the gravitational force between two objects
        """
        r = np.sqrt(np.sum((self.position - other_obj_position)**2))
        force_magnitude = (G * M_SUN * self.mass) / r**2
        force_direction = (other_obj_position - self.position) / r
        force = force_magnitude * force_direction
        return force

    def update_position_velocity(self, time):
        """
            New position/ velocity along the way
        """
        force = self.gravitational_force(np.array([0, 0]))  # Gravitational force from the Sun
        acceleration = force / self.mass
        self.velocity += acceleration * time
        self.position += self.velocity * time
        return self.position

##################################
# Initial conditions for Mercury #
##################################

M_MERCURY = 0.330e24 # mass
initial_position_mercury = [0.387 * AU, 0.0]
initial_velocity_mercury = [0.0, 47400.0]

# Initial conditions for Venus
M_VENUS = 4.87e24 # mass
initial_position_venus = [0.723 * AU, 0.0]
initial_velocity_venus = [0.0, 35000.0]

################################
# Initial conditions for Earth #
################################

M_EARTH = 5.972e24 # mass
initial_position_earth = [AU, 0.0]
initial_velocity_earth = [0.0, 29800.0]

# Initial conditions for Mars
M_MARS = 0.642e24 # mass
initial_position_mars = [1.52* AU, 0.0]
initial_velocity_mars = [0.0, 24100.0]

############################
# Create celestial objects #
############################

sun = CelestialObject(M_SUN, [0, 0], [0, 0], 'red', 'Sun')
mercury = CelestialObject(
    M_MERCURY,
    initial_position_mercury,
    initial_velocity_mercury, 'gray', 'Mercury')
venus = CelestialObject(
    M_VENUS,
    initial_position_venus,
    initial_velocity_venus, 'white', 'Venus'
)
earth = CelestialObject(
    M_EARTH,
    initial_position_earth,
    initial_velocity_earth, 'blue', 'Earth')
mars = CelestialObject(
    M_MARS,
    initial_position_mars,
    initial_velocity_mars, 'brown', 'Mars'
)

##############
# Simulation #
##############
mercury_positions = np.zeros((N_STEPS, 2))
venus_positions = np.zeros((N_STEPS, 2))
earth_positions = np.zeros((N_STEPS, 2))
mars_positions = np.zeros((N_STEPS, 2))

mercury_positions[0] = initial_position_mercury
venus_positions[0] = initial_position_venus
earth_positions[0] = initial_position_earth
mars_positions[0] = initial_position_mars

for step in range(1, N_STEPS):
    mercury_positions[step] = mercury.update_position_velocity(DAY_TIME)
    venus_positions[step] = venus.update_position_velocity(DAY_TIME)
    earth_positions[step] = earth.update_position_velocity(DAY_TIME)
    mars_positions[step] = mars.update_position_velocity(DAY_TIME)

#############
# Animation #
#############

fig, ax = plt.subplots()

# Mercury
mercury_dot, = ax.plot([], [], 'o', color=mercury.color)
orbit_mercury, = ax.plot([], [], '-', color='white', lw=0.5)
text_mercury = ax.text(
    mercury.position[0],
    mercury.position[1],
    mercury.name, fontsize=8,
    color=mercury.color)

# Venus
venus_dot, = ax.plot([], [], 'o', color=venus.color)
orbit_venus, = ax.plot([], [], '-', color='white', lw=0.5)
text_venus = ax.text(
    venus.position[0],
    venus.position[1],
    venus.name, fontsize=8,
    color=venus.color
)

# Earth
earth_dot, = ax.plot([], [], 'o', color=earth.color)
orbit_earth, = ax.plot([], [], '-', color='white', lw=0.5)
text_earth = ax.text(
    earth.position[0],
    earth.position[1],
    earth.name,
    fontsize=8,
    color=earth.color)

# Mars
mars_dot, = ax.plot([], [], 'o', color=mars.color)
orbit_mars, = ax.plot([], [], '-', color='white', lw=0.5)
text_mars = ax.text(
    mars.position[0],
    mars.position[1],
    mars.name,
    fontsize = 8,
    color=mars.color
)

# The sun
sun_dot, = ax.plot(sun.position[0], sun.position[1], 'ro', markersize=10)

# Set x and y limits directly
ax.set_xlim(-3 * AU, 3 * AU)
ax.set_ylim(-3 * AU, 3 * AU)
ax.axis("off")

def update(frame):
    """
        Animation
    """

    x_mercury, y_mercury = mercury_positions[frame]
    mercury_dot.set_data(x_mercury, y_mercury)
    text_mercury.set_position((x_mercury, y_mercury))
    orbit_mercury.set_data(mercury_positions[:frame, 0], mercury_positions[:frame, 1])

    x_venus, y_venus = venus_positions[frame]
    venus_dot.set_data(x_venus, y_venus)
    text_venus.set_position((x_venus, y_venus))
    orbit_venus.set_data(venus_positions[:frame, 0], venus_positions[:frame, 1])

    x_earth, y_earth = earth_positions[frame]
    earth_dot.set_data(x_earth, y_earth)
    text_earth.set_position((x_earth, y_earth))
    orbit_earth.set_data(earth_positions[:frame, 0], earth_positions[:frame, 1])

    x_mars, y_mars = mars_positions[frame]
    mars_dot.set_data(x_mars, y_mars)
    text_mars.set_position((x_mars, y_mars))
    orbit_mars.set_data(mars_positions[:frame, 0], mars_positions[:frame, 1])

    return (sun_dot, mercury_dot, venus_dot, earth_dot, mars_dot,
            text_mercury, text_venus, text_earth,  text_mars,
            orbit_earth, orbit_mercury, orbit_venus, orbit_mars
            )

animation = FuncAnimation(fig, update, frames=N_STEPS, blit=True, interval=10)

# Save the animation as a gif file
animation.save('solar_system.gif', dpi=200)
# plt.show()
