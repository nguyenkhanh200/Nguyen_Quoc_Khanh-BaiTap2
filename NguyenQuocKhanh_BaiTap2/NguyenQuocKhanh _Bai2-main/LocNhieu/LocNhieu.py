import cv2
import os

# Đọc ảnh ở chế độ màu (mặc định)
image = cv2.imread('anhra.jpg')

# Tạo thư mục lưu ảnh nếu chưa tồn tại
output_folder = 'dau ra'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 5. Lọc nhiễu Gaussian trên ảnh màu
gaussian_filtered_image_color = cv2.GaussianBlur(image, (3, 3), 0)
cv2.imwrite(os.path.join(output_folder, 'anh loc nhieu.jpg'), gaussian_filtered_image_color)

print(f"Ảnh đã được lưu vào thư mục: {output_folder}")
