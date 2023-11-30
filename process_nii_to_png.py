import nibabel as nib
import matplotlib.pyplot as plt
import os
import numpy as np

def process_medical_images_with_segmentation(image_folder, seg_folder, output_folder):
    # Create the output folders for images and labels if they don't exist
    images_output_folder = os.path.join(output_folder, 'images')
    labels_output_folder = os.path.join(output_folder, 'labels')
    
    if not os.path.exists(images_output_folder):
        os.makedirs(images_output_folder)
    if not os.path.exists(labels_output_folder):
        os.makedirs(labels_output_folder)

    # List the files in the image folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.nii.gz') and not f.startswith('._')]
    # Process each image and its corresponding segmentation
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        seg_file = image_file.replace('image', 'label')  # Assuming a naming convention where 'image' is replaced by 'label' for segmentation files
        seg_path = os.path.join(seg_folder, seg_file)

        # Load the NIfTI files
        image = nib.load(image_path)
        segmentation = nib.load(seg_path)

        # Get the data from the files
        image_data = image.get_fdata()
        seg_data = segmentation.get_fdata()

        # Normalize the image data for visualization
        image_data = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data))

        # Iterate over each slice
        for i in range(image_data.shape[2]):
            # Save the image slice
            fig_img, ax_img = plt.subplots()
            ax_img.imshow(image_data[:, :, i], cmap='gray')
            ax_img.axis('off')
            output_image_path = os.path.join(images_output_folder, f"{image_file[:-7]}_slice_{i}.png")
            fig_img.savefig(output_image_path, bbox_inches='tight', pad_inches=0)
            plt.close(fig_img)
            
            # Save the segmentation slice
            fig_seg, ax_seg = plt.subplots()
            ax_seg.imshow(seg_data[:, :, i], cmap='jet')
            ax_seg.axis('off')
            output_seg_path = os.path.join(labels_output_folder, f"{seg_file[:-7]}_slice_{i}.png")
            fig_seg.savefig(output_seg_path, bbox_inches='tight', pad_inches=0)
            plt.close(fig_seg)

# Example usage
image_folder = './Task06_Lung/imagesTr'
seg_folder = './Task06_Lung/labelsTr'
output_folder = './processed'
process_medical_images_with_segmentation(image_folder, seg_folder, output_folder)
