import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

measurements_tilsiter = [12.0, 12.5, 13.0, 13.0, 13.0, 13.5, 11.5, 12.0]
measurements_butterkase = [12.0, 12.0, 13.0, 13.5, 11.5, 13.0, 13.0]
measurements_gouda = [12.0, 13.0, 13.0, 12.0, 12.0, 13.0]

# Box plot
plt.boxplot([measurements_tilsiter, measurements_butterkase, measurements_gouda], labels=['Tilsiter', 'Butterkäse', 'Gouda'])
plt.title('Verschiedene Käsesorten Box plot')
plt.ylabel('Abstand (cm)')
plt.savefig('experiment-4-box.png', dpi=300)

# Violin plot
plt.figure()
plt.violinplot([measurements_tilsiter, measurements_butterkase, measurements_gouda])
plt.xticks([1, 2, 3], ['Tilsiter', 'Butterkäse', 'Gouda'])
plt.title('Verschiedene Käsesorten Violin plot')
plt.ylabel('Abstand (cm)')
plt.savefig('experiment-4-violin.png', dpi=300)

# Histogram
bin_edges_tilsiter = np.linspace(11, 14, 12) - 0.05  # offset to visualize overlap
bin_edges_butterkase = np.linspace(11, 14, 12)
bin_edges_gouda = np.linspace(11, 14, 12) + 0.05

plt.figure()
plt.hist(measurements_tilsiter, bins=bin_edges_tilsiter, alpha=0.5, label='Tilsiter')
plt.hist(measurements_butterkase, bins=bin_edges_butterkase, alpha=0.5, label='Butterkäse')
plt.hist(measurements_gouda, bins=bin_edges_gouda, alpha=0.5, label='Gouda')
plt.xlabel('Abstand (cm)')
plt.ylabel('Häufigkeit')
plt.title('Verschiedene Käsesorten Histogram')
plt.legend()
plt.savefig('experiment-4-histogram.png', dpi=300)

# Performing an ANOVA test to compare the three groups
f_statistic, p_value = stats.f_oneway(measurements_tilsiter, measurements_butterkase, measurements_gouda)  # 0.02, 0.98

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")