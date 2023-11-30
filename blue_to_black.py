import os
from PIL import Image
import numpy as np

def process_images(input_dir, output_dir):
    """
    Processes all images in the input directory, changing blue and gray to black and everything else to red, 
    then saves them to the output directory.

    :param input_dir: The directory containing the images to process.
    :param output_dir: The directory where the processed images will be saved.
    """

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct full file path
            file_path = os.path.join(input_dir, filename)
            # Open the image
            image = Image.open(file_path)
            # Convert image to numpy array
            image_array = np.array(image)

            # Sample colors for blue and gray from the image
            blue_color_sample = np.array([0, 0, 127])
            gray_color_sample = np.array([128, 128, 128])

            # Create masks for blue and gray colors using the sampled values
            blue_mask = (image_array[:, :, 0] == blue_color_sample[0]) & (image_array[:, :, 1] == blue_color_sample[1]) & (image_array[:, :, 2] == blue_color_sample[2])
            gray_mask = (image_array[:, :, 0] == gray_color_sample[0]) & (image_array[:, :, 1] == gray_color_sample[1]) & (image_array[:, :, 2] == gray_color_sample[2])

            # Change blue and gray colors to black, and everything else to red
            image_array[blue_mask | gray_mask] = [0, 0, 0]  # Change to black
            image_array[~(blue_mask | gray_mask)] = [255, 0, 0]  # Change everything else to red

            # Convert array back to image
            modified_image = Image.fromarray(image_array)

            # Save the modified image to the output directory
            modified_image_path = os.path.join(output_dir, filename)
            modified_image.save(modified_image_path)

# Example usage:
process_images('/home/jorge/Desktop/tdt17/data/masksUsedToMakeLabels', '/home/jorge/Desktop/tdt17/new_data/new_masks')

# Please replace 'path/to/input_directory' and 'path/to/output_directory' with your actual directory paths.
# Here, we are just defining the function, not running it. You need to call this function with your specific directories.
