from ultralytics import YOLO

model = YOLO('yolov8m-seg.pt')  # load a pretrained model (recommended for training)

results = model.train(data='config.yaml', epochs=300, imgsz=384)