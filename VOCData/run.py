from ultralytics import YOLO

# Load a model
model = YOLO("yolov8MSFF_CBAM.yaml").load('yolov8l.pt')#添加cbam和msff
#model = YOLO("yolov8MSFF.yaml").load('yolov8l.pt')#只添加msff
#model = YOLO("yolov8MSFF_cbam.yaml").load('yolov8l.pt')#只添加cbam
#model = YOLO('yolov8x.pt')


results =model.train(data="D:/pythondaima/my_yolov8-main/ultralytics/cfg/datasets/myvoc.yaml", epochs=150, imgsz=640, device=[0,], workers=0, batch=16, cache=True)  # train the model

