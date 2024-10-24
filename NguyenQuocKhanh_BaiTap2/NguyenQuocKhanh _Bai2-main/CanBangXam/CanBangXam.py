import cv2
import numpy as np
import os

# Kiểm tra thư mục làm việc hiện tại
print("Thư mục làm việc hiện tại:", os.getcwd())

# Đường dẫn tuyệt đối đến tệp ảnh (cập nhật đường dẫn cho phù hợp)
# Đường dẫn mới sau khi đã giải nén tệp ZIP
image_path = r'C:\Users\khanh\Downloads\Truong_Van_Phuong_Quyen_Bai2-main\CanBangXam\toi'
 # Thay thế đường dẫn chính xác tới tệp ảnh của bạn

# Đọc ảnh màu từ đường dẫn
image = cv2.imread(image_path)

# Kiểm tra xem ảnh có được đọc thành công hay không
if image is None:
    print(f"Không thể đọc được ảnh từ đường dẫn: {image_path}")
    print("Vui lòng kiểm tra đường dẫn hoặc tệp ảnh.")
    exit()  # Thoát khỏi chương trình nếu không đọc được ảnh

# Tạo thư mục lưu ảnh nếu chưa tồn tại
output_folder = 'dau ra'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 1. Tách các kênh màu (RGB)
(B, G, R) = cv2.split(image)

# 2. Tính trung bình của từng kênh
mean_B = np.mean(B)
mean_G = np.mean(G)
mean_R = np.mean(R)

# 3. Tính giá trị trung bình của cả ba kênh
mean_gray = (mean_B + mean_G + mean_R) / 3

# 4. Điều chỉnh các kênh màu theo giá trị trung bình
B = np.clip(B * (mean_gray / mean_B), 0, 255).astype(np.uint8)
G = np.clip(G * (mean_gray / mean_G), 0, 255).astype(np.uint8)
R = np.clip(R * (mean_gray / mean_R), 0, 255).astype(np.uint8)

# 5. Gộp lại các kênh đã điều chỉnh thành ảnh màu mới
balanced_image = cv2.merge([B, G, R])

# Lưu ảnh đã cân bằng xám
output_path = os.path.join(output_folder, 'anh can bang xam.jpg')
cv2.imwrite(output_path, balanced_image)

print(f"Ảnh đã được lưu vào thư mục: {output_folder}")
