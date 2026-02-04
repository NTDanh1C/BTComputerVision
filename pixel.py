import matplotlib.pyplot as plt
import numpy as np
import cv2

# Kích thước ảnh
height = 768   # chiều cao (số hàng)
width = 1024   # chiều rộng (số cột)

# Tạo ảnh màu
img = np.zeros((height, width, 3), dtype=np.uint8)

# Gán pixel (ví dụ: random màu để thấy rõ từng pixel)
for i in range(height):
    for j in range(width):
        img[i, j, 0] = np.random.randint(0, 256)  # Blue
        img[i, j, 1] = np.random.randint(0, 256)  # Green
        img[i, j, 2] = np.random.randint(0, 256)  # Red

# Hiển thị bằng Matplotlib (BGR -> RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("Image size: 1024 x 768")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

n=500
img = np.zeros((n,n),dtype=np.uint8)
for i in range(n):
    img[i,i]=255
plt.imshow(img, cmap='PuRd')
plt.show()