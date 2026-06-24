import os

# 定义两个文件夹路径
folder1_path = 'D:\pythondaima\my_yolov8-main\VOCData\labels'
folder2_path = 'D:\pythondaima\my_yolov8-main\VOCData\data_v1(剔除前)\labels_full'

# 获取文件夹1中所有文件的文件名列表
files_in_folder1 = [f for f in os.listdir(folder1_path) if os.path.isfile(os.path.join(folder1_path, f))]

# 遍历文件夹1中的文件名列表
for file_name in files_in_folder1:
    # 构建文件夹2中的文件路径
    file_path_in_folder2 = os.path.join(folder2_path, file_name)
    # 如果文件夹2中存在相同的文件名，则删除该文件
    if os.path.isfile(file_path_in_folder2):
        os.remove(file_path_in_folder2)
        print(f"Removed: {file_path_in_folder2}")
    else:
        print(f"File not found: {file_path_in_folder2}")