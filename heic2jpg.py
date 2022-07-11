import os
from PIL import  Image
import cv2
import shutil
import numpy as np
from tqdm import tqdm
import pillow_heif

def copy_file(source_path,des_path):#复制操作
    if not os.path.exists(des_path):
        shutil.copy2(source_path, des_path)
    else:
        pass

# 读图片文件， 这种方式能读取路径中含有中文的图像文件
def imread(path):
    image_array = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)  #
    return image_array

# 存图片文件
def imsave(path, image):
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imencode('.png', image)[1].tofile(path)

#判断是否是苹果手机拍摄的实时照片
def is_apple_device(file_name):
    if os.path.splitext(file_name)[-1] == ".livp" or os.path.splitext(file_name)[-1] == ".LIVP" or os.path.splitext(file_name)[-1] == ".heic":
        return True
    else:
        return False


def heic_to_jpg(img_item,img_source,livp_to_jpg_dir):
    img_id = img_item.split('.')[0]
    heif_file = pillow_heif.read_heif(img_source)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )

    jpg_save_path = os.path.join(livp_to_jpg_dir, img_id + '.jpg')
    image.save(jpg_save_path, format="jpeg")

if __name__ == '__main__':

    heic_dir = r'D:\wood\heic'
    heic_to_jpg_dir = r'D:\wood\jpg'

    img_list = os.listdir(heic_dir)
    for img_item in tqdm(img_list):
        print(img_item)
        img_source = os.path.join(heic_dir,img_item)
        img_destination = os.path.join(heic_to_jpg_dir,img_item)
        heic_to_jpg(img_item, img_source, heic_to_jpg_dir)
