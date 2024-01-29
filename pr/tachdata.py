import re

def convert_to_normalized_format(x_min, y_min, width, height, image_width, image_height):
    center_x = (x_min + 0.5 * width) / image_width
    center_y = (y_min + 0.5 * height) / image_height
    normalized_width = width / image_width
    normalized_height = height / image_height
    return center_x, center_y, normalized_width, normalized_height

def extract_image_size(filename):
    match = re.match(r"\d+ (\d+) (\d+)", filename)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None

def process_and_convert(file_content):
    lines = file_content.split('\n')
    image_sizes = {}
    bounding_boxes = []

    current_image = None
    for line in lines:
        if line.startswith("0--Parade"):
            current_image = line.strip()
        elif current_image is not None and re.match(r"\d+ \d+ \d+ \d+", line):
            width, height = extract_image_size(current_image)
            if width is not None and height is not None:
                image_sizes[current_image] = (width, height)
                bounding_boxes.append(line.strip())

    converted_bounding_boxes = []
    for bbox_info in bounding_boxes:
        x_min, y_min, width, height, *rest = map(int, bbox_info.split())
        center_x, center_y, normalized_width, normalized_height = convert_to_normalized_format(
            x_min, y_min, width, height, image_sizes[current_image][0], image_sizes[current_image][1]
        )
        converted_bounding_boxes.append(f"0 {center_x} {center_y} {normalized_width} {normalized_height} {' '.join(map(str, rest))}")

    return image_sizes, converted_bounding_boxes

def export_to_file(output_file_name, image_sizes, bounding_boxes):
    with open(output_file_name, 'w') as output_file:
        # Ghi thông tin kích thước ảnh
        for image_name, size in image_sizes.items():
            output_file.write(f"{image_name}: {size[0]} x {size[1]}\n")

        # Ghi thông tin bounding boxes đã chuyển đổi
        for bbox_info in bounding_boxes:
            output_file.write(f"{bbox_info}\n")

output_file_name = 'ten_tep_moi.txt'  # Thay thế tên tệp mới theo ý muốn của bạn

# Đọc nội dung từ tệp txt
with open('29--Students_Schoolkids.txt', 'r') as file:
    file_content = file.read()

# Xử lý dữ liệu, chuyển đổi và xuất vào tệp mới
image_sizes, bounding_boxes = process_and_convert(file_content)
export_to_file(output_file_name, image_sizes, bounding_boxes)

print(f"Xuất dữ liệu đã chuyển đổi vào tệp {output_file_name}")
