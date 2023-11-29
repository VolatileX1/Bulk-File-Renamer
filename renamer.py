import os

def bulk_rename(folder_path, operation, new_value):
    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)

        for file_name in files:
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
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} to {new_path}")
            else:
                print(f"Skipped: {old_path}")

    except FileNotFoundError:
        print(f"Error: Folder not found - {folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
folder_path = "/path/to/your/folder"
operation = "suffix"  # Change to "prefix" or "change_extension" as needed
new_value = "_new"

bulk_rename(folder_path, operation, new_value)
