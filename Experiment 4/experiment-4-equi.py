import numpy as np
from statsmodels.stats.weightstats import ttost_ind

measurements_tilsiter = [12.0, 12.5, 13.0, 13.0, 13.0, 13.5, 11.5, 12.0]
measurements_butterkase = [12.0, 12.0, 13.0, 13.5, 11.5, 13.0, 13.0]
measurements_gouda = [12.0, 13.0, 13.0, 12.0, 12.0, 13.0]

all_measurements = measurements_tilsiter + measurements_butterkase + measurements_gouda

margin = 1  # 1 cm, typical to choose double the measurment error

# Tilsiter vs. Butterkäse
tost_tb = ttost_ind(measurements_tilsiter, measurements_butterkase, -margin, margin)

# Tilsiter vs. Gouda
tost_tg = ttost_ind(measurements_tilsiter, measurements_gouda, -margin, margin)

# Butterkäse vs. Gouda
tost_bg = ttost_ind(measurements_butterkase, measurements_gouda, -margin, margin)

# Output the results
tost_results = {
    "Tilsiter vs. Butterkäse": tost_tb[2][1],
    "Tilsiter vs. Gouda": tost_tg[2][1],
    "Butterkäse vs. Gouda": tost_bg[2][1]
}

print(tost_results)