# Bulk File Renamer

A Python script for bulk renaming files in a folder based on prefix, suffix, or changing extensions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Bulk File Renamer is a handy Python script that allows you to rename multiple files in a folder simultaneously. Whether you need to add a prefix, suffix, or change file extensions, this script simplifies the process and saves you time.

## Features

- **Prefix**: Add a specified prefix to the beginning of each file name.
- **Suffix**: Add a specified suffix to the end of each file name.
- **Change Extension**: Replace the existing file extension with a new one.
- **Batch Renaming**: Rename multiple files with a common prefix or suffix in one go.
- **Interactive Mode**: Interactive mode for user confirmation before each renaming operation.
- **Logging**: Log the details of each renaming operation for future reference.
- **Case Insensitivity**: Case-insensitive comparison for the operation parameter.
- **Error Handling**: Improved error handling for folder not found and general exceptions.
- **Skip Option**: Option to skip individual files during the renaming process.
- **Filtering Files**: Allow users to specify a filter for the files to be processed based on file extensions or patterns.
- **Recursive Operation**: Add an option to perform the operation recursively on subdirectories within the specified folder.
- **Dry Run Mode**: Provide an option for a "dry run" where the script prints what changes would be made without actually renaming the files.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bulk-file-renamer.git

2. Navigate to the project directory:

   ```bash
   cd bulk-file-renamer

3. Modify the script parameters in the bulk_rename.py file:

- folder_path: Path to the folder containing the files you want to rename.
- operation: Choose "prefix", "suffix", or "change_extension".
- new_value: Specify the new prefix, suffix, or extension.

4. Run the script:

   ```bash
   python renamer.py

## Contributing

If you have suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.
