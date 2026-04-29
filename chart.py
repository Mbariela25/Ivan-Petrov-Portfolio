import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

weights = [55, 35, 7, 3]
values = [275000, 175000, 35000, 15000]
colors = ['#1B3A6B', '#4A7C9E', '#C49A2C', '#B0B8C1']
explode = (0.03, 0.03, 0.03, 0.03)

fig, ax = plt.subplots(figsize=(10, 7.5), facecolor='white')

wedges, _, _ = ax.pie(
    weights,
    labels=None,
    autopct='',
    colors=colors,
    explode=explode,
    startangle=90,
    wedgeprops=dict(edgecolor='white', linewidth=2.5),
    shadow=False,
    radius=1.0,
)

centre_circle = plt.Circle((0, 0), 0.58, fc='white')
ax.add_artist(centre_circle)

ax.text(0, 0.10, '€500,000', ha='center', va='center',
        fontsize=17, fontweight='bold', color='#1B3A6B',
        fontfamily='serif')
ax.text(0, -0.12, 'Total Portfolio', ha='center', va='center',
        fontsize=11, color='#666666', fontfamily='sans-serif')

for wedge, weight in zip(wedges, weights):
    angle = (wedge.theta2 + wedge.theta1) / 2
    r = 0.78
    x = r * np.cos(np.radians(angle))
    y = r * np.sin(np.radians(angle))
    ax.text(x, y, f'{weight}%', ha='center', va='center',
            fontsize=13, fontweight='bold', color='white')

legend_labels = [
    'Equities — 55%  (€275,000)',
    'Fixed Income — 35%  (€175,000)',
    'Real Assets — 7%  (€35,000)',
    'Cash — 3%  (€15,000)',
]
patches = [
    mpatches.Patch(facecolor=colors[i], edgecolor='#dddddd', linewidth=0.5, label=legend_labels[i])
    for i in range(4)
]
ax.legend(
    handles=patches,
    loc='lower center',
    bbox_to_anchor=(0.5, -0.18),
    ncol=2,
    fontsize=11,
    frameon=False,
    handlelength=1.4,
    handleheight=1.0,
)

ax.set_title(
    'Ivan Petrov Portfolio Allocation – April 2026',
    fontsize=14, fontweight='bold', color='#1B3A6B',
    pad=22, y=1.04, fontfamily='serif',
)

plt.tight_layout()
plt.savefig('portfolio_allocation.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("Saved: portfolio_allocation.png")
