import os
import shutil

def bulk_rename(folder_path=None, operation=None, new_value=None, filter_ext=None, recursive=False, dry_run=False):
    try:
        if folder_path is None:
            folder_path = os.getcwd()

        # Get the list of files in the folder
        files = []

        if recursive:
            for root, dirs, filenames in os.walk(folder_path):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
        else:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        for file_name in files:
            # Filter files based on extension or pattern
            if filter_ext and not file_name.endswith(filter_ext):
                continue

            # Construct the old and new file paths
            old_path = os.path.join(folder_path, file_name)

            # Extract the file extension
            base_name, extension = os.path.splitext(file_name)

            if operation.lower() == "prefix":
                new_name = f"{new_value}{file_name}"
            elif operation.lower() == "suffix":
                new_name = f"{base_name}{new_value}{extension}"
            elif operation.lower() == "change_extension":
                new_name = f"{base_name}.{new_value}"

            new_path = os.path.join(folder_path, new_name)

            # Confirm the renaming operation
            user_input = input(f"Rename {old_path} to {new_path}? (y/n): ").lower()

            if user_input == "y":
                if not dry_run:
                    # Rename the file
                    shutil.move(old_path, new_path)
                print(f"Renamed: {old_path} to {new_path}")
            else:
                print(f"Skipped: {old_path}")

    except FileNotFoundError:
        print(f"Error: Folder not found - {folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# If folder_path is not provided, it defaults to the current working directory
operation = "suffix"  # Change to "prefix" or "change_extension" as needed
new_value = "_new"

# Additional Features
filter_ext = ".txt"  # Filter files with a specific extension
recursive = True  # Perform operation recursively on subdirectories
dry_run = False  # Set to True for a dry run (no actual file modifications)

bulk_rename(operation=operation, new_value=new_value, filter_ext=filter_ext, recursive=recursive, dry_run=dry_run)
