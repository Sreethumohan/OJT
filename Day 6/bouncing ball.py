#Write a python program to generate an animation of an elastic ball droping from a height and after it touches the ground it is bouncing.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # gravity (m/s^2)
e = 0.9   # coefficient of restitution (elasticity)
dt = 0.01 # time step (s)
y0 = 10   # initial height (m)
v0 = 0    # initial velocity (m/s)

# Initial conditions
y = y0
v = v0

# Lists to store the ball's position
y_vals = [y]

# Function to update the ball's position
def update_ball():
    global y, v
    v += -g * dt
    y += v * dt
    if y <= 0:
        y = 0
        v = -e * v
    y_vals.append(y)

# Animation function
def animate(frame):
    update_ball()
    ball.set_data([0], [y_vals[-1]])  # Update ball position
    return ball,

# Setting up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, y0 + 1)
ax.set_aspect('equal')
ax.grid()

# Creating the ball
ball, = ax.plot([], [], 'o', markersize=20)

# Creating the animation
ani = FuncAnimation(fig, animate, frames=500, interval=dt*1000, blit=True)

# Display the animation
plt.show()
