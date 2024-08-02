import os
import re
import shutil

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def load_data(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):
        for file_name in sorted(files):
            _, file_extension = os.path.splitext(file_name)

            subdir = subdir.replace(f"{source_path}/", "")

            year = re.findall(r"\b\d{4}\b", file_name)[-1]
            month = re.findall(r"\b\d{2}\b", file_name)[-1]

            # Make results path
            os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

            source_file_path = os.path.join(source_path, subdir, file_name)
            results_file_path = os.path.join(results_path, subdir, file_name)

            # Check if file needs to be loaded
            if clean or not os.path.exists(results_file_path):
                shutil.copyfile(source_file_path, results_file_path)

                if not quiet:
                    print(f"✓ Load {file_name}")
            else:
                print(f"✓ Already exists {subdir}/{file_name}")
