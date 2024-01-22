import matplotlib.pyplot as plt
import scipy.stats as stats

measurements_hinten = [15.0, 9.0, 14.5, 9.0]
measurements_mitte = [12.0, 14.0, 13.0, 13.0, 13.0, 12.5, 14.0, 12.5]
measurements_vorne = [13.0, 13.0, 13.0, 12.5, 9.0, 14.0, 13.5]

# Box plot
plt.boxplot([measurements_hinten, measurements_mitte, measurements_vorne], labels=['Hinten', 'Mitte', 'Vorne'])
plt.title('Verschiedene Käse-Positionierungen Box plot')
plt.ylabel('Abstand (cm)')
plt.savefig('experiment-2-box.png', dpi=300)

# Violin plot
plt.figure()
plt.violinplot([measurements_hinten, measurements_mitte, measurements_vorne])
plt.xticks([1, 2, 3], ['Hinten', 'Mitte', 'Vorne'])
plt.title('Verschiedene Käse-Positionierungen Violin plot')
plt.ylabel('Abstand (cm)')
plt.savefig('experiment-2-violin.png', dpi=300)

# Histogram
plt.figure()
plt.hist(measurements_hinten, alpha=0.5, label='Hinten', bins=5)
plt.hist(measurements_mitte, alpha=0.5, label='Mitte', bins=5)
plt.hist(measurements_vorne, alpha=0.5, label='Vorne', bins=5)
plt.xlabel('Abstand (cm)')
plt.ylabel('Häufigkeit')
plt.title('Verschiedene Käse-Positionierungen Histogram')
plt.legend()
plt.savefig('experiment-2-histogram.png', dpi=300)

# Performing an ANOVA test to compare the three groups
f_statistic, p_value = stats.f_oneway(measurements_hinten, measurements_mitte, measurements_vorne)  # 0.51, 0.61

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

