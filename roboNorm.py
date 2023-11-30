import os
import re

def rename_files(directory):
    # Regular expression to match and extract the numbers from file names
    pattern = re.compile(r'lung_(\d+)_slice_(\d+)')

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            match = pattern.search(filename)
            if match:
                # Extracting numbers from the file name
                lung_number = int(match.group(1))
                slice_number = int(match.group(2))

                # Constructing the new file name
                new_filename = f"lung_{lung_number:03d}_slice_{slice_number}.txt"
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)

                # Renaming the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")

# Usage
directory = 'C:/Users/jorge/Desktop/tdt17/tmpLabels'  # Replace with the path to your directory
rename_files(directory)
