from scipy import stats
import numpy as np

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