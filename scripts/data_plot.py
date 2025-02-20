import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Plotting
plt.figure(figsize=(10, 6))

# Subplot 1: Time vs Dipole values
plt.subplot(2, 1, 1)
plt.plot(time, dipole_gen['Dipole_X'], color=arylide_yellow, linewidth=1.5, label='$D_{gen_x}$')
plt.plot(time, dipole_gen['Dipole_Y'], color=ball_blue, linewidth=1.5, label='$D_{gen_y}$')
plt.plot(time, dipole_gen['Dipole_Z'], color=brick_red, linewidth=1.5, label='$D_{gen_z}$')
plt.grid(True)
plt.box(True)
plt.ylabel('$[Am^2]$', fontsize=14)
plt.title('Dipole Generated', fontsize=14)
plt.legend(fontsize=14)
plt.axis([time.iloc[0], time.iloc[-1], -130, 130])

# Subplot 2: Time vs Reaction Wheels Speeds (RPM)
plt.subplot(2, 1, 2)
plt.plot(time, w_rw_rpm['RW1_Speed'], color=arylide_yellow, linewidth=1.5, label='$\omega_{rw_1}$')
plt.plot(time, w_rw_rpm['RW2_Speed'], color=ball_blue, linewidth=1.5, label='$\omega_{rw_2}$')
plt.plot(time, w_rw_rpm['RW3_Speed'], color=brick_red, linewidth=1.5, label='$\omega_{rw_3}$')
plt.plot(time, w_rw_rpm['RW4_Speed'], color=camouflage_green, linewidth=1.5, label='$\omega_{rw_4}$')
plt.grid(True)
plt.box(True)
plt.ylabel('[RPM]', fontsize=14)
plt.xlabel('Time [s]', fontsize=14)
plt.title('RWs Speed', fontsize=14)
plt.legend(fontsize=14)
plt.axis([time.iloc[0], time.iloc[-1], -6500, 6500])

plt.tight_layout()


# Plotting spacecraft angular rates and norm
plt.figure(figsize=(10, 6))

# Subplot 1: Time vs Spacecraft Angular Rates (deg/s)
plt.subplot(2, 1, 1)
plt.plot(time, sc_rate_deg['SC_Rate_X'], color=arylide_yellow, linewidth=1.5, label='$\omega_x$')
plt.plot(time, sc_rate_deg['SC_Rate_Y'], color=ball_blue, linewidth=1.5, label='$\omega_y$')
plt.plot(time, sc_rate_deg['SC_Rate_Z'], color=brick_red, linewidth=1.5, label='$\omega_z$')
plt.grid(True)
plt.box(True)
plt.ylabel('[deg/s]', fontsize=14)
plt.title('Spacecraft Angular Rates ($\omega_x, \omega_y, \omega_z$)', fontsize=14)
plt.legend(fontsize=14)

# Subplot 2: Time vs Spacecraft Angular Rate Norm (deg/s)
plt.subplot(2, 1, 2)
plt.plot(time, sc_rate_norm_deg, color=camouflage_green, linewidth=1.5, label='$||\omega||$')
plt.grid(True)
plt.box(True)
plt.ylabel('[deg/s]', fontsize=14)
plt.xlabel('Time [s]', fontsize=14)
plt.title('Spacecraft Angular Rate Norm', fontsize=14)
plt.legend(fontsize=14)

plt.tight_layout()
plt.show()
