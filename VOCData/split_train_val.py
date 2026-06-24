# coding:utf-8

import os
import random
import argparse

parser = argparse.ArgumentParser()
# txt 文件的地址，根据自己的数据进行修改
parser.add_argument('--txt_path', default='labels', type=str, help='input txt label path')
# 数据集的划分输出路径，地址选择自己数据下的 ImageSets/Main
parser.add_argument('--output_path', default='ImageSets/Main', type=str, help='output txt label path')
opt = parser.parse_args()

trainval_percent = 1.0  # 训练集和验证集所占比例。 这里没有划分测试集
train_percent = 0.85     # 训练集所占比例，可自己进行调整
txtfilepath = opt.txt_path
txtsavepath = opt.output_path

# 获取所有的 txt 文件
total_txt = [f for f in os.listdir(txtfilepath) if f.endswith('.txt')]
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_txt)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)

# 分别创建 trainval.txt、test.txt、train.txt 和 val.txt
file_trainval = open(os.path.join(txtsavepath, 'trainval.txt'), 'w')
file_test = open(os.path.join(txtsavepath, 'test.txt'), 'w')
file_train = open(os.path.join(txtsavepath, 'train.txt'), 'w')
file_val = open(os.path.join(txtsavepath, 'val.txt'), 'w')

# 根据文件名划分数据集
for i in list_index:
    name = total_txt[i][:-4] + '\n'  # 去掉 .txt 后缀
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_trainval.close()
file_train.close()
file_val.close()
file_test.close()
