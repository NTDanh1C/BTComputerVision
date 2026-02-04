import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

size = 600
center = size // 2
radius = 250

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, size)
ax.set_ylim(0, size)
ax.set_aspect('equal')
ax.axis("off")

# 🔥 QUAN TRỌNG: đảo trục Y → đúng hệ đồng hồ
ax.invert_yaxis()

# Nền trắng
ax.imshow(np.ones((size, size, 3)))

# =========================
# Số La Mã đúng vị trí
# =========================
roman_numbers = [
    "XII", "I", "II", "III", "IV", "V",
    "VI", "VII", "VIII", "IX", "X", "XI"
]

angles = np.deg2rad(np.arange(12) * 30 - 90)

for roman, angle in zip(roman_numbers, angles):
    x = center + radius * np.cos(angle)
    y = center + radius * np.sin(angle)
    ax.text(x, y, roman, ha='center', va='center',
            fontsize=18, fontweight='bold')

# =========================
# Kim đồng hồ
# =========================
hour_hand, = ax.plot([], [], lw=6)
minute_hand, = ax.plot([], [], lw=4)
second_hand, = ax.plot([], [], lw=2, color='red')

# =========================
# Animation – tốc độ BÌNH THƯỜNG
# =========================
def update(frame):
    sec = frame % 60
    minute = (frame // 60) % 60
    hour = (frame // 3600) % 12

    # 🔥 KHÔNG cần đảo dấu nữa
    sec_angle = np.deg2rad(sec * 6 - 90)
    min_angle = np.deg2rad(minute * 6 - 90)
    hour_angle = np.deg2rad(hour * 30 - 90)

    second_hand.set_data(
        [center, center + radius * 0.9 * np.cos(sec_angle)],
        [center, center + radius * 0.9 * np.sin(sec_angle)]
    )

    minute_hand.set_data(
        [center, center + radius * 0.75 * np.cos(min_angle)],
        [center, center + radius * 0.75 * np.sin(min_angle)]
    )

    hour_hand.set_data(
        [center, center + radius * 0.5 * np.cos(hour_angle)],
        [center, center + radius * 0.5 * np.sin(hour_angle)]
    )

    return hour_hand, minute_hand, second_hand

ani = FuncAnimation(
    fig,
    update,
    frames=3600,
    interval=1000   # 1 giây / frame
)

plt.title("Roman Clock – Correct Clockwise Motion")
plt.show()
