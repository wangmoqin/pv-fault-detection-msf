# -*- coding: utf-8 -*-
import os
from os import getcwd

sets = ['train', 'val', 'test']
abs_path = os.getcwd()
print(abs_path)

# 你可以根据需要保留或去除 convert 函数
# 这里的函数没有实际调用，但你可以决定是否删除
def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h

wd = getcwd()

for image_set in sets:
    # 确保输出文件夹存在
    if not os.path.exists('D:/pythondaima/my_yolov8-main/VOCData/labels/'):
        os.makedirs('D:/pythondaima/my_yolov8-main/VOCData/labels/')
    image_ids = open('D:/pythondaima/my_yolov8-main/VOCData/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()

    if not os.path.exists('D:/pythondaima/my_yolov8-main/VOCData/dataSet_path/'):
        os.makedirs('D:/pythondaima/my_yolov8-main/VOCData/dataSet_path/')

    # 打开并生成文件路径列表
    list_file = open('D:/pythondaima/my_yolov8-main/VOCData/dataSet_path/%s.txt' % (image_set), 'w')
    # 根据 image_id 生成文件路径并写入 list_file
    for image_id in image_ids:
        list_file.write('D:/pythondaima/my_yolov8-main/VOCData/images/%s.jpg\n' % (image_id))
    list_file.close()
