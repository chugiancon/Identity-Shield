from PIL import Image
import os

def save_image_sizes_to_txt(directory_path, output_file):
    with open(output_file, 'w') as txt_file:
        # Lặp qua tất cả các tệp trong thư mục
        for filename in os.listdir(directory_path):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Có thể thêm các định dạng ảnh khác nếu cần
                image_path = os.path.join(directory_path, filename)
                try:
                    # Mở ảnh và lấy kích thước
                    with Image.open(image_path) as img:
                        width, height = img.size
                        # Ghi thông tin vào tệp tin văn bản
                        txt_file.write(f"{filename}: {width} x {height}\n")
                except Exception as e:
                    print(f"Không thể đọc kích thước ảnh {filename}: {str(e)}")

# Thay đổi đường dẫn thư mục đầu vào và tên tệp tin văn bản đầu ra tùy thuộc vào yêu cầu của bạn
directory_path = "E:\\MTCNN\\chơi\\Data\\29--Students_Schoolkids"
output_file = "kichthuoc_anh.txt"

save_image_sizes_to_txt(directory_path, output_file)
