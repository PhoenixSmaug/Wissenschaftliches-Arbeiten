from scipy import stats
import numpy as np
import matplotlib.pyplot as plt 

# Given frequency
frequency = 2450 * 10**6  # MHz to Hz

# Wavelength measurements
wavelength_measurements = [
    13.0, 12.5,
    12.0,
    14.0, 14.0,
    12.0,
    13.0, 13.0, 12.0, 14.0,
    11.5, 12.0, 13.0, 13.0
]
# Convert from cm to m
wavelength_measurements = [x * 10**-2 for x in wavelength_measurements]

speed_of_light_measurements = [frequency * wavelength for wavelength in wavelength_measurements]

mean_speed_of_light = np.mean(speed_of_light_measurements)

sem_speed_of_light = stats.sem(speed_of_light_measurements)

# Calculate the confidence interval for alpha = 0.01
confidence_interval = stats.t.interval(0.99, len(speed_of_light_measurements)-1, loc=mean_speed_of_light, scale=sem_speed_of_light)

print(mean_speed_of_light)
print(sem_speed_of_light)
print(confidence_interval)

wavelength_measurements_cm = np.array(wavelength_measurements) * 100.0
wavelength_measurements_cm = np.round(wavelength_measurements_cm, 3)

true_speed_of_light = 299792458

plt.figure(figsize=(10, 5)) 
unique_wavelengths, counts = np.unique(wavelength_measurements_cm, return_counts=True)
sizes = counts * 30  # Scale up the sizes for better visibility

for i, wavelength in enumerate(unique_wavelengths):
    matching_speeds = [speed for speed, wave in zip(speed_of_light_measurements, wavelength_measurements_cm) if wave == wavelength]
    plt.scatter([wavelength] * len(matching_speeds), matching_speeds, s=sizes[i], label=f'{wavelength} cm ({counts[i]})')

# Mark the true speed of light
plt.axhline(y=true_speed_of_light, color='r', linestyle='-', label='True Speed of Light')

# Labeling the plot
plt.title('Calculated Speed of Light vs. Measured Wavelength')
plt.xlabel('Wavelength (cm)')
plt.ylabel('Calculated Speed of Light (m/s)')
plt.legend()
plt.grid(True)

plt.savefig('experiment-1.png', dpi=300)
