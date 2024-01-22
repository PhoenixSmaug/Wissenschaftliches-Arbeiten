import matplotlib.pyplot as plt
import scipy.stats as stats

measurements_500 = [11.5, 12.0, 13.5, 14.0, 12.0, 14.0, 13.5, 12.0, 13.0, 14.0]
measurements_900 = [13.0, 13.0, 13.0, 12.5, 13.0, 12.5, 12.5, 12.0, 13.0]

# Box plot
plt.boxplot([measurements_500, measurements_900], labels=['500 W', '900 W'])
plt.title('Verschiedene Mikrowellen-Stufen Box plot')
plt.ylabel('Abstand (cm)')
plt.savefig('experiment-3-box.png', dpi=300)

# Violin plot
plt.figure()
plt.violinplot([measurements_500, measurements_900])
plt.xticks([1, 2], ['500 W', '900 W'])
plt.title('Verschiedene Mikrowellen-Stufen Violin plot')
plt.ylabel('Abstand (cm)')
plt.savefig('experiment-3-violin.png', dpi=300)

# Historgram
plt.figure()
plt.hist(measurements_500, alpha=0.5, label='500 W', bins=5)
plt.hist(measurements_900, alpha=0.5, label='900 W', bins=5)
plt.xlabel('Abstand (cm)')
plt.ylabel('Häufigkeit')
plt.title('Verschiedene Mikrowellen-Stufen Histogram')
plt.savefig('experiment-3-histogram.png', dpi=300)

# Performing a t-test to compare the two groups
t_statistic, p_value = stats.ttest_ind(measurements_500, measurements_900, equal_var=False)  # 0.68, 0.51

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
