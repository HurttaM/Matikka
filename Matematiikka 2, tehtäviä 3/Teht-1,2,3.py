from matplotlib import pyplot as plt, patches
import numpy as np

fig, ax = plt.subplots(figsize=(18, 6))

ymp = patches.Circle((0, 0), radius=1, fill=False, edgecolor="black")
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Asetetaan asteikko välille -3π ja 3π sekä määritellään akselien merkintäarvot ja nimet
ax.set_xlim(-3 * np.pi, 3 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Akselien merkintäarvot radiaaneina
x_ticks = [-3 * np.pi, -2 * np.pi, -1 * np.pi, 0, 1 * np.pi, 2 * np.pi, 3 * np.pi]
x_labels = [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$']
y_ticks = [-1, -0.5, 0, 0.5, 1]
y_labels = [r'$-1$', r'$-0.5$', r'$0$', r'$0.5$', r'$1$']

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)

# Määritellään pisteiden kulmat radiaaneina ja vastaavat merkit
angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = [np.radians(angle) for angle in angles_deg]
angle_labels = [
    r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$',
    r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$', r'$\pi$', r'$\frac{3\pi}{2}$'
]

# Piirretään pisteet ja niiden merkit ympyrän kehässä
for rad, label in zip(angles_rad, angle_labels):
    x, y = np.cos(rad), np.sin(rad)
    plt.scatter(x, y, color="purple", marker='X')  # Vaihdettu väri
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(10, 10), ha='center')

# Piirretään käyrät -3π ja 3π välille sinille ja cosinille
x_vals = np.linspace(-3 * np.pi, 3 * np.pi, 500)
y_sin = np.sin(x_vals)
y_cos = np.cos(x_vals)

# Piirretään sin- ja cos-käyrät uudella värillä ja tyylillä
ax.plot(x_vals, y_sin, label="sin(x)", color="blue", linestyle="--")
ax.plot(x_vals, y_cos, label="cos(x)", color="green", linestyle="-.")

# Lisätään selite
ax.legend(loc="upper right")

plt.show()