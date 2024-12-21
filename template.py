# Importing necessary modules
import os  # For interacting with the operating system (e.g., creating directories, files)
from pathlib import Path  # For filesystem path manipulation
import logging  # For logging messages during program execution

# Configuring logging to display messages with timestamps
logging.basicConfig(
    level=logging.INFO,  # Log level set to INFO; will log messages with INFO or higher severity
    format='[%(asctime)s]: %(message)s:'  # Log message format with a timestamp and the message
)

# Defining the project name as a variable
project_name = "ChickenDiseaseClassifier"

# Listing all the files and directories to be created for the project
list_of_files = [
    ".github/workflows/.gitkeep",  # Placeholder file for an empty workflows directory
    f"src{project_name}/__init__.py",  # Makes src/ChickenDiseaseClassifier a Python package
    f"src{project_name}/components/__init__.py",  # Package initialization for components module
    f"src{project_name}/utils/__init__.py",  # Package initialization for utils module
    f"src{project_name}/config/__init__.py",  # Package initialization for config module
    f"src{project_name}/config/configuration.py",  # Configuration file for handling project settings
    f"src{project_name}/pipeline/__init__.py",  # Package initialization for pipeline module
    f"src{project_name}/entity/__init__.py",  # Package initialization for entity module
    f"src{project_name}/constants/__init__.py",  # Package initialization for constants module
    "config/config.yaml",  # YAML file for configuration settings
    "dvc.yaml",  # DVC pipeline configuration file
    "params.yaml",  # Parameters for the ML model or pipeline
    "requirements.txt",  # File for listing Python dependencies
    "setup.py",  # Python package setup file for project installation
    "research/trials.ipynb"  # Jupyter notebook for experimentation or prototyping
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Creating a Path object from the filepath
    filedir, filename = os.path.split(filepath)  # Splitting the filepath into directory and filename
    if filedir != "":  # If the directory is not empty
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # If the file doesn't exist or is empty
        with open(filepath, "w") as f:  # Open the file in write mode
            pass
            logging.info(f"Creating empty file: {filepath}")
            
            
    else:
        logging.info(f"{filename} already exists")