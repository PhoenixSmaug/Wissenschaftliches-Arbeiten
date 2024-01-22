import numpy as np
from statsmodels.stats.weightstats import ttost_ind

measurements_hinten = [15.0, 9.0, 14.5, 9.0]
measurements_mitte = [12.0, 14.0, 13.0, 13.0, 13.0, 12.5, 14.0, 12.5]
measurements_vorne = [13.0, 13.0, 13.0, 12.5, 9.0, 14.0, 13.5]

all_measurements = measurements_hinten + measurements_mitte + measurements_vorne
#margin = 1
margin = 1.5

# Nicht signifikant äquivalent für 1 cm, aber mit 2 cm

# Hinten vs. Mitte
tost_hm = ttost_ind(measurements_hinten, measurements_mitte, -margin, margin)

# Hinten vs. Vorne
tost_hv = ttost_ind(measurements_hinten, measurements_vorne, -margin, margin)

# Mitte vs. Vorne
tost_mv = ttost_ind(measurements_mitte, measurements_vorne, -margin, margin)

# Output the results
tost_results = {
    "Hinten vs. Mitte": tost_hm[2][1],
    "Hinten vs. Vorne": tost_hv[2][1],
    "Mitte vs. Vorne": tost_mv[2][1]
}

print(tost_results)

