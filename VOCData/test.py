import cv2
from ultralytics import YOLO

# 加载训练好的模型
model = YOLO(r"D:\pythondaima\my_yolov8-main\best.pt")  # 替换为你的模型路径

# 输入图像路径
image_path = r"D:\pythondaima\my_yolov8-main\testdata\.jpg"  # 替换为你的图片路径

# 使用模型进行预测
results = model(image_path)

# 读取原始图像
img = cv2.imread(image_path)

# 获取预测结果并解析
max_detections = 13  # 设置最大检测框数量
for result in results:
    boxes = result.boxes.xyxy  # 得到边界框坐标 (x1, y1, x2, y2)
    confidences = result.boxes.conf  # 得到置信度
    classes = result.boxes.cls  # 得到分类

    # 计算检测出的目标数量
    num_detections = len(boxes)
    print(f'检测到的目标数量: {num_detections}')

    # 在图片上绘制每个检测到的目标框，限制最多绘制 max_detections 个框
    for i, (box, confidence, cls) in enumerate(zip(boxes, confidences, classes)):
        if i >= max_detections:  # 超过最大检测数量时停止绘制
            break
        x1, y1, x2, y2 = map(int, box)  # 转换坐标为整数
        class_name = result.names[int(cls)]  # 获取类别名称

        # 绘制边界框
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 绿色边框，宽度为2

        # 在边界框上方显示类别和置信度
        label = f'{class_name} {confidence:.2f}'
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 输出类别和置信度信息
        print(f'类别: {class_name}, 置信度: {confidence:.2f}')

# 保存带有检测框的图像
output_path = r'D:\pythondaima\my_yolov8-main\testdata\1号duibi.jpg'
cv2.imwrite(output_path, img)

print(f"检测完成，结果已保存到 {output_path}")
