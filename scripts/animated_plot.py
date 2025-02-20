import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Define colors
arylide_yellow = [0.910000, 0.840000, 0.420000]
ball_blue = [0.130000, 0.670000, 0.800000]
brick_red = [0.800000, 0.250000, 0.330000]
camouflage_green = [0.470000, 0.530000, 0.420000]
rads2rpm = 60 / (2 * np.pi)  # Conversion factor from rad/s to RPM
rads2deg = 180 / np.pi  # Conversion factor from rad/s to deg/s

# Load the CSV file using pandas to handle headers
data = pd.read_csv("./data/sim_out.csv")

# Parse the data
time = data['Time']
dipole_gen = data[['Dipole_X', 'Dipole_Y', 'Dipole_Z']]  # Dipole values
w_rw = data[['RW1_Speed', 'RW2_Speed', 'RW3_Speed', 'RW4_Speed']]  # Reaction wheels speeds in rad/s
sc_rate = data[['SC_Rate_X', 'SC_Rate_Y', 'SC_Rate_Z']]  # Spacecraft angular rates
sc_rate_norm = data['SC_Rate_Norm']

# Transform RW speeds to RPM
w_rw_rpm = w_rw * rads2rpm

# Transform spacecraft rates to deg/s
sc_rate_deg = sc_rate * rads2deg
sc_rate_norm_deg = sc_rate_norm * rads2deg

# Animation settings
animation_duration = 40  # Total duration of the animation in seconds (change this value to adjust speed)
fps = 30  # Frames per second
total_frames = animation_duration * fps

# Set up the figure and axes
fig, axs = plt.subplots(2, 2, figsize=(12, 8))  # Increased figsize for better spacing
fig.suptitle("Actuators vs SC Rotation Rate", fontsize=20, y=0.95)  # Adjusted y-position for better spacing

# Subplot 1: Time vs Dipole values
ax1 = axs[0, 0]
lines1 = [
    ax1.plot([], [], color=arylide_yellow, linewidth=1.5, label='$D_{gen_x}$')[0],
    ax1.plot([], [], color=ball_blue, linewidth=1.5, label='$D_{gen_y}$')[0],
    ax1.plot([], [], color=brick_red, linewidth=1.5, label='$D_{gen_z}$')[0]
]
ax1.set_xlim(time.iloc[0], time.iloc[-1])
ax1.set_ylim(-130, 130)
ax1.set_title('Dipole Generated', fontsize=14)
ax1.set_ylabel('$[Am^2]$', fontsize=12)
ax1.grid(True)
ax1.legend()

# Subplot 2: Time vs Reaction Wheels Speeds (RPM)
ax2 = axs[0, 1]
lines2 = [
    ax2.plot([], [], color=arylide_yellow, linewidth=1.5, label='$\omega_{rw_1}$')[0],
    ax2.plot([], [], color=ball_blue, linewidth=1.5, label='$\omega_{rw_2}$')[0],
    ax2.plot([], [], color=brick_red, linewidth=1.5, label='$\omega_{rw_3}$')[0],
    ax2.plot([], [], color=camouflage_green, linewidth=1.5, label='$\omega_{rw_4}$')[0]
]
ax2.set_xlim(time.iloc[0], time.iloc[-1])
ax2.set_ylim(-6500, 6500)
ax2.set_title('RWs Speed', fontsize=14)
ax2.set_ylabel('[RPM]', fontsize=12)
ax2.grid(True)
ax2.legend()

# Subplot 3: Time vs Spacecraft Angular Rates (deg/s)
ax3 = axs[1, 0]
lines3 = [
    ax3.plot([], [], color=arylide_yellow, linewidth=1.5, label='$\omega_x$')[0],
    ax3.plot([], [], color=ball_blue, linewidth=1.5, label='$\omega_y$')[0],
    ax3.plot([], [], color=brick_red, linewidth=1.5, label='$\omega_z$')[0]
]
ax3.set_xlim(time.iloc[0], time.iloc[-1])
ax3.set_ylim(sc_rate_deg.min().min(), sc_rate_deg.max().max())
ax3.set_title('Spacecraft Angular Rates', fontsize=14)
ax3.set_ylabel('[deg/s]', fontsize=12)
ax3.grid(True)
ax3.legend()

# Subplot 4: Time vs Spacecraft Angular Rate Norm (deg/s)
ax4 = axs[1, 1]
line4 = ax4.plot([], [], color=camouflage_green, linewidth=1.5, label='$||\omega||$')[0]
ax4.set_xlim(time.iloc[0], time.iloc[-1])
ax4.set_ylim(sc_rate_norm_deg.min(), sc_rate_norm_deg.max())
ax4.set_title('Spacecraft Angular Rate Norm', fontsize=14)
ax4.set_ylabel('[deg/s]', fontsize=12)
ax4.grid(True)
ax4.legend()

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Leave space for the suptitle

# Alternatively, you can use subplots_adjust for more control:
# fig.subplots_adjust(top=0.92, hspace=0.4, wspace=0.3)

# Animation function
def animate(frame):
    # Calculate the fraction of the data to show
    idx = int(frame / total_frames * len(time))  # Map frame (0-total_frames) to time index
    
    # Update Dipole plots
    for line, col in zip(lines1, dipole_gen.columns):
        line.set_data(time[:idx], dipole_gen[col][:idx])
    
    # Update Reaction Wheels Speeds plots
    for line, col in zip(lines2, w_rw_rpm.columns):
        line.set_data(time[:idx], w_rw_rpm[col][:idx])
    
    # Update Spacecraft Angular Rates plots
    for line, col in zip(lines3, sc_rate_deg.columns):
        line.set_data(time[:idx], sc_rate_deg[col][:idx])
    
    # Update Spacecraft Angular Rate Norm plot
    line4.set_data(time[:idx], sc_rate_norm_deg[:idx])
    
    return lines1 + lines2 + lines3 + [line4]

# Set up animation
ani = FuncAnimation(fig, animate, frames=total_frames, interval=1000 / fps, blit=True, repeat=False)

# Save the animation as an MP4 file
writer = FFMpegWriter(fps=fps, metadata={'title': 'Simulated Data Animation'}, bitrate=1800)
ani.save("simulated_data_animation.mp4", writer=writer)

plt.show()
