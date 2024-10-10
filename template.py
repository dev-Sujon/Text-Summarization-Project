import os  # Importing the 'os' module to interact with the operating system
from pathlib import Path  # Importing 'Path' from 'pathlib' for easier handling of file paths
import logging  # Importing logging to log information, warnings, errors, etc.

# Configuring the logging system to display messages at INFO level and format them with a timestamp
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Specify the project name, which will be used to create folders and files inside 'src/'
project_name = "textSummarizer"

# A list of file paths to be created, using the project_name variable where needed
list_of_files = [
    ".github/workflows/.gitkeep",  # Special file for GitHub workflows, used to keep empty folders
    f"src/{project_name}/__init__.py",  # Initializing 'textSummarizer' package
    f"src/{project_name}/components/__init__.py",  # Initializing 'components' subpackage
    f"src/{project_name}/utils/__init__.py",  # Initializing 'utils' subpackage
    f"src/{project_name}/utils/common.py",  # 'common.py' will contain utility functions
    f"src/{project_name}/logging/__init__.py",  # Initializing 'logging' subpackage
    f"src/{project_name}/config/__init__.py",  # Initializing 'config' subpackage
    f"src/{project_name}/config/configuration.py",  # Configuration logic will be here
    f"src/{project_name}/pipeline/__init__.py",  # Initializing 'pipeline' subpackage
    f"src/{project_name}/entity/__init__.py",  # Initializing 'entity' subpackage
    f"src/{project_name}/constants/__init__.py",  # Initializing 'constants' subpackage
    f"src/{project_name}",  # Creating main 'textSummarizer' folder
    "config/config.yaml",  # Configuration file in YAML format
    "params.yaml",  # Parameters file in YAML format
    "app.py",  # Main application file
    "Dockerfile", # Dockerfile to containerize the project
    "requirements.txt",  # Python dependencies will be listed here
    "setup.py",  # Script for packaging and distribution
    "test.py",
    "research/test.ipynb"  # Jupyter notebook for experimentation
]

# Iterating over the list of files to create them
for filepath in list_of_files:
    file_path = Path(filepath)  # Convert the string path to a Path object for easier manipulation
    file_dir, file_name = os.path.split(file_path)  # Split the path into directory and filename

    # If the directory path is not empty, ensure the directory exists, create it if it doesn't
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)  # Create the directory, if it already exists, do nothing
        logging.info(f"Creating directory: {file_dir} for the file {file_name}")  # Log directory creation

    # Check if the file doesn't exist or is empty, then create an empty file
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(filepath, "w") as f:  # Open the file in write mode, creating it if necessary
            pass  # No need to write anything, just create an empty file
        logging.info(f"Creating empty file {filepath}")  # Log file creation
    else:
        # If the file already exists and is not empty, log that information
        logging.info(f"{file_name} already exists")
        
        
        
        
        
### Name of the Work: **Project Directory and File Structure Initialization Script**
### Pseudocode:

#1. **Import necessary modules**:
#   - Import `os` for interacting with the operating system.
#   - Import `Path` from `pathlib` for handling file paths.
#   - Import `logging` to log information at different levels (INFO, WARNING, ERROR).

#2. **Set up logging configuration**:
#   - Configure logging to display `INFO` level messages with timestamps.

#3. **Define the project name**:
#   - Set the variable `project_name` to the name of the project (e.g., "textSummarizer").

#4. **Create a list of files and directories**:
#   - Define `list_of_files`, which contains:
#     - Folder paths for directories to be created.
#     - File paths with file extensions for necessary files within the project structure (e.g., Python files, YAML configuration files, Dockerfile, etc.).

#5. **Iterate over the list of files**:
#   - For each `filepath` in the `list_of_files`:
#     - Convert `filepath` into a `Path` object for easy file and directory handling.
#     - Split the `filepath` into `file_dir` (directory part) and `file_name` (file name part).

#6. **Check if the directory exists**:
#   - If `file_dir` is not an empty string:
#     - Use `os.makedirs()` to create the directory if it doesn’t already exist.
#     - Log the creation of the directory with a message.

#7. **Check if the file exists or is empty**:
#   - If the file does not exist or has zero size:
#     - Open the file in write mode to create an empty file.
#     - Log the creation of the empty file.
#   - Otherwise, log that the file already exists and skip creation.

#8. **End of script**:
#   - All directories and files are created as specified in the list, ensuring that the project structure is initialized.

#### Simplified Pseudocode:

#1. **Import modules**: `os`, `pathlib.Path`, `logging`.
#2. **Configure logging**: Set logging level to INFO.
#3. **Define project name**: `"textSummarizer"`.
#4. **Create file list**: List of directories and files needed for the project.
#5. **For each file in the list**:
#   - Split into directory and file name.
#   - If directory exists, skip; if not, create it.
#   - If file exists and is non-empty, skip; if not, create it.
#6. **Log actions**: Log file and directory creation or existence.
