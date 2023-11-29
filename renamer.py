import os

def bulk_rename(folder_path, operation, new_value):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    for file_name in files:
        # Construct the old and new file paths
        old_path = os.path.join(folder_path, file_name)

        # Extract the file extension
        base_name, extension = os.path.splitext(file_name)

        if operation == "prefix":
            new_name = f"{new_value}{file_name}"
        elif operation == "suffix":
            new_name = f"{base_name}{new_value}{extension}"
        elif operation == "change_extension":
            new_name = f"{base_name}.{new_value}"

        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} to {new_path}")

# Example usage:
folder_path = "/path/to/your/folder"
operation = "suffix"  # Change to "prefix" or "change_extension" as needed
new_value = "_new"

bulk_rename(folder_path, operation, new_value)
