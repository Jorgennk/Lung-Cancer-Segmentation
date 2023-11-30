import cv2
import numpy as np
from ultralytics import YOLO
import os
from tqdm import tqdm

# Load the YOLOv8 model
model_path = "/home/jorge/Desktop/tdt17/runs/segment/train/weights/best.pt"
model = YOLO(model_path)

# Define the source folder and output folder
source_folder = "/home/jorge/Desktop/imagesTs/images/images"
output_folder = "/home/jorge/Desktop/imagesTs/predict"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process all images in the source folder
for image_file in tqdm(os.listdir(source_folder), desc="Processing images"):
    if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            # Load the image
            image_path = os.path.join(source_folder, image_file)
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Unable to read image {image_file}")

            # Perform the prediction
            results = model.predict(img)

            # Check if masks are available in the result
            if results[0].masks is not None:
                # Extract the first mask
                mask_raw = results[0].masks[0].cpu().data.numpy().transpose(1, 2, 0)
                mask_single_channel = mask_raw[:, :, 0]  # Take only one channel
                h2, w2, _ = results[0].orig_img.shape
                mask = cv2.resize(mask_single_channel, (w2, h2))

                # Convert the mask to 8-bit unsigned integer
                mask = (mask * 255).astype(np.uint8)

                # Lower the threshold or adjust as necessary
                if np.count_nonzero(mask) > 0.001 * mask.size:  # Adjust the threshold as necessary
                    # Apply the mask to the original image
                    masked_image = cv2.bitwise_and(img, img, mask=mask)

                    # Save the masked image
                    output_path = os.path.join(output_folder, f"masked_{image_file}")
                    if not cv2.imwrite(output_path, masked_image):
                        raise ValueError(f"Unable to write image to {output_path}")
                else:
                    print(f"No significant mask for image {image_file}. Skipping.")
        except Exception as e:
            print(f"Error processing image {image_file}: {e}")
