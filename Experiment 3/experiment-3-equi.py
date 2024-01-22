import numpy as np
from statsmodels.stats.weightstats import ttost_ind

measurements_500 = [11.5, 12.0, 13.5, 14.0, 12.0, 14.0, 13.5, 12.0, 13.0, 14.0]
measurements_900 = [13.0, 13.0, 13.0, 12.5, 13.0, 12.5, 12.5, 12.0, 13.0]

all_measurements = measurements_500 + measurements_900

# Define the margin as 1 cm, which is double the assumed measurement error of 0.5 cm
margin = 1  # 1 cm

# Perform TOST for 500 W vs. 900 W
tost_500_900 = ttost_ind(measurements_500, measurements_900, -margin, margin)

# Output the result
tost_results = {
    "500 W vs. 900 W": tost_500_900[2][1]
}

print(tost_results)