# Simple attempt at Task06_Lung for the Medical Segmentation Decathlon


It is worth noting that this is just an attempt and they results weren't extraordinary good. It was however able to detect most of the cancer cases in the Lungs and provide good segmentations where it was discovered.

![](l2gif.gif) ![](l8gif.gif)


*The gif is glitchy, there was abug when covnerting the .pngs to a gif using a script*


## Model
I used a YOLOv8m segmentation model for this task. One known issue of the YOLO models are its ability to detect small blobs, this might be where the lack of recall stems from.