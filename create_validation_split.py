import os
import shutil
import random

def move_files_for_body(body, src_dir, dest_dir):
    for file in os.listdir(src_dir):
        if file.startswith(body):
            shutil.move(os.path.join(src_dir, file), dest_dir)

def main():
    images_train_dir = "/home/jorge/Desktop/tdt17/new_data/images/train"
    images_val_dir = "/home/jorge/Desktop/tdt17/new_data/images/val"
    labels_train_dir = "/home/jorge/Desktop/tdt17/new_data/labels/train"
    labels_val_dir = "/home/jorge/Desktop/tdt17/new_data/labels/val"

    # Collect all unique bodies in the training images directory
    bodies = set()
    for file in os.listdir(images_train_dir):
        if file.startswith("lung_"):
            body_id = file.split('_slice')[0]
            bodies.add(body_id)

    # Convert bodies set to a list
    bodies_list = list(bodies)

    # Select a subset of bodies for validation
    num_to_select = len(bodies_list) // 5  # for example, 20% of the dataset
    selected_bodies = random.sample(bodies_list, num_to_select)

    # Move image and label files of selected bodies to validation folders
    for body in selected_bodies:
        move_files_for_body(body, images_train_dir, images_val_dir)
        move_files_for_body(body, labels_train_dir, labels_val_dir)

    print(f"Moved {len(selected_bodies)} bodies to validation set.")

if __name__ == "__main__":
    main()
