import random

import cv2
import string
import os

input_path = "C://Users//ThomasLe//PycharmProjects//AIFaceRecogCam//input"
output_path = "C://Users//ThomasLe//PycharmProjects//AIFaceRecogCam//output"

def adjustBrightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    
    if value >= 0:
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
    else:
        lim = abs(value)
        v[v < lim] = 0
        v[v >= lim] -= abs(value)
    
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def adjustContrast(img, value):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=value, tileGridSize=(8,8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl,a,b))

    enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return enhanced_img

def randomName(char_num):
    full_name = []
    for _ in range(char_num):
        full_name.append(random.choice(string.ascii_letters + string.digits))
    print("".join(full_name))
    return ''.join(full_name)

def ImageAugmentation(copy = 1, flip = False, brightness = 0, contrast = 0):
    print
    for file in os.listdir(input_path):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".webp"):
            for _ in range(copy):
                img = cv2.imread(os.path.join(input_path, file))
                # Flip
                if flip:
                    img = cv2.flip(img, 1)
                # Brightness
                img = adjustBrightness(img, brightness)
                # Contrast
                img = adjustContrast(img, contrast)
                # Save output
                cv2.imwrite(os.path.join(output_path, randomName(6) + "." + file.split(".")[-1]), img)

if __name__ == "__main__":
    ImageAugmentation(1, False, 20, 4)