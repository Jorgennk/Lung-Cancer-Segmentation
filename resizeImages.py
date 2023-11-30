import os
from PIL import Image
from tqdm import tqdm

def resize_images_in_folder_with_progress(folder_path, new_size=(384, 384), background_color="gray"):
    """
    Resize all images in the given folder to the specified size, adding a plain color padding.
    The padding is added evenly to all sides of each image. Displays a progress bar.

    Args:
    folder_path (str): Path to the folder containing the images.
    new_size (tuple): The desired size (width, height) for the resized images.
    background_color (str): The color of the padding. Default is gray.

    Returns:
    None
    """
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for filename in tqdm(image_files, desc="Processing images"):
        # Load the image
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Calculate padding
        left = (new_size[0] - image.width) // 2
        top = (new_size[1] - image.height) // 2
        right = new_size[0] - image.width - left
        bottom = new_size[1] - image.height - top

        # Create a new image with the specified background color
        new_image = Image.new("RGB", new_size, background_color)
        new_image.paste(image, (left, top))

        # Save the new image, optionally to a new path or overwrite the old one
        new_image.save(image_path)

# Example usage
resize_images_in_folder_with_progress('/home/jorge/Desktop/imagesTs/images/images')  # Replace with your folder path
# This script will resize all images in the specified folder and display a progress bar.
