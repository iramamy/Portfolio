"""
    Import useful packages
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')
fig, ax = plt.subplots()

# Constants
G = 6.67430e-11
M_SUN = 1.989e30
AU = 1.496e11
DAY_TIME = 60 * 60 * 24
TOTAL_TIME = 365 * 24 * 60 * 60 * 2
N_STEPS = int(TOTAL_TIME / DAY_TIME)

# Initial conditions for Mercury
M_MERCURY = 0.330e24  # mass
initial_position_mercury = [0.387 * AU, 0.0]
initial_velocity_mercury = [0.0, 47400.0]

# Initial conditions for Venus
M_VENUS = 4.87e24 # mass
initial_position_venus = [0.723 * AU, 0.0]
initial_velocity_venus = [0.0, 35000.0]

# Initial conditions for Earth

M_EARTH = 5.972e24 # mass
initial_position_earth = [AU, 0.0]
initial_velocity_earth = [0.0, 29800.0]

# Initial conditions for Mars
M_MARS = 0.642e24 # mass
initial_position_mars = [1.52* AU, 0.0]
initial_velocity_mars = [0.0, 24100.0]

class CelestialObject:
    """
        Solar system object
    """
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

    def simulate_motion(self):
        """
            Update the position of each object
        """
        positions = np.zeros((N_STEPS, 2))
        positions[0] = self.position
        for step in range(1, N_STEPS):
            positions[step] = self.update_position_velocity(DAY_TIME)
        return positions

    def plot_object(self):
        """
            Plot the dot and the orbit of an object
        """
        object_dot, = ax.plot([], [], 'o', color=self.color)
        object_orbit, = ax.plot([], [], '-', color='white', lw=0.5)
        object_text = ax.text(
            self.position[0],
            self.position[1],
            self.name, fontsize=8,
            color = self.color
        )
        return object_dot, object_orbit, object_text

def main():
    '''
        Main function
    '''
    # Create celestial objects

    #Sun
    sun = CelestialObject(M_SUN, [0, 0], [0, 0], 'red', 'Sun')

    # Mercury
    mercury = CelestialObject(
        M_MERCURY,
        initial_position_mercury,
        initial_velocity_mercury, 'gray', 'Mercury'
    )
    mercury_dot, mercury_orbit, mercury_text = mercury.plot_object()
    mercury_positions = mercury.simulate_motion()

    # Venus
    venus = CelestialObject(
    M_VENUS,
        initial_position_venus,
        initial_velocity_venus, 'white', 'Venus'
    )
    venus_dot, venus_orbit, venus_text = venus.plot_object()
    venus_positions = venus.simulate_motion()

    # Earth
    earth = CelestialObject(
    M_EARTH,
        initial_position_earth,
        initial_velocity_earth, 'blue', 'Earth'
    )
    earth_dot, earth_orbit, earth_text = earth.plot_object()
    earth_positions = earth.simulate_motion()

    # Mars
    mars = CelestialObject(
        M_MARS,
        initial_position_mars,
        initial_velocity_mars, 'brown', 'Mars'
    )
    mars_dot, mars_orbit, mars_text = mars.plot_object()
    mars_positions = mars.simulate_motion()

    # Simulation
    _, = ax.plot(sun.position[0], sun.position[1], 'ro', markersize=10)

    def update(frame):
        # Animate mercury
        mercury_x, mercury_y = mercury_positions[frame]
        mercury_dot.set_data(mercury_x, mercury_y)
        mercury_text.set_position((mercury_x, mercury_y))
        mercury_orbit.set_data(mercury_positions[:frame, 0], mercury_positions[:frame, 1])

        venus_x, venus_y = venus_positions[frame]
        venus_dot.set_data(venus_x, venus_y)
        venus_text.set_position((venus_x, venus_y))
        venus_orbit.set_data(venus_positions[:frame, 0], venus_positions[:frame, 1])

        earth_x, earth_y = earth_positions[frame]
        earth_dot.set_data(earth_x, earth_y)
        earth_text.set_position((earth_x, earth_y))
        earth_orbit.set_data(earth_positions[:frame, 0], earth_positions[:frame, 1])

        mars_x, mars_y = mars_positions[frame]
        mars_dot.set_data(mars_x, mars_y)
        mars_text.set_position((mars_x, mars_y))
        mars_orbit.set_data(mars_positions[:frame, 0], mars_positions[:frame, 1])
        return (
            mercury_dot, mercury_text, mercury_orbit,
            venus_dot, venus_text, venus_orbit,
            earth_dot, earth_text, earth_orbit,
            mars_dot, mars_text, mars_orbit
            )

    #
    anim = FuncAnimation(fig, update, frames=N_STEPS, interval=10)

    # Set x and y limits directly
    ax.set_xlim(-3 * AU, 3 * AU)
    ax.set_ylim(-3 * AU, 3 * AU)
    ax.axis("off")

    # Save the animation as a gif file
    anim.save('solar_system.gif', dpi=200)
    plt.show()

if __name__ == "__main__":
    main()
