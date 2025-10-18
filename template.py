# os aur pathlib libraries import kar rahe hain taake file system ke sath kaam kar saken
import os
from pathlib import Path

# logging module se logs generate karne ke liye setup kar rahe hain
# ye har step ka timestamp ke sath message print karega
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# yahan project ka naam define kar rahe hain
project_name = "datascience"

# ye list me hum saare folders aur files define kar rahe hain jo project me automatically create honge
list_of_files = [
    ".gthub/workflows/.gitkeep",                     # GitHub workflows folder ke andar ek placeholder file
    f"src/{project_name}/__init__.py",               # src ke andar main project folder aur uska init file
    f"src/{project_name}/components/__init__.py",    # components folder (model training/testing modules ke liye)
    f"src/{project_name}/utils/__init__.py",         # utils folder (helper functions ke liye)
    f"src/{project_name}/utils/common.py",           # common utility functions rakhnay ke liye file
    f"src/{project_name}/config/__init__.py",        # config folder (configuration files aur scripts)
    f"src/{project_name}/config/configuration.py",   # configuration handle karne ke liye main python file
    f"src/{project_name}/pipeline/__init__.py",      # pipeline folder (training aur prediction pipeline)
    f"src/{project_name}/entity/__init__.py",        # entity folder (data classes aur entities store karne ke liye)
    f"src/{project_name}/entity/config_entity.py",   # config entities define karne ke liye file
    f"src/{project_name}/constants/__init__.py",     # constants folder (constant variables ke liye)
    "config/config.yaml",                            # configuration file (paths aur parameters store karne ke liye)
    "params.yaml",                                   # parameters file (ML model parameters)
    "schema.yaml",                                   # data schema define karne ke liye file
    "main.py",                                       # project ka main entry point (execution start yahan se hoti hai)
    "Dockerfile",                                    # Docker containerization ke liye
    "setup.py",                                      # package setup aur installation handle karta hai
    "research/research.ipynb",                       # Jupyter Notebook research experiments ke liye
    "templates/index.html",                          # Flask web app ka frontend template
    "app.py"                                         # Flask application ka main backend file
]

# ab hum ek loop me saare files/folders create kar rahe hain
for filepath in list_of_files:
    # Path object me convert karte hain taake OS-independent path mile
    filepath = Path(filepath)

    # filedir aur filename ko alag kar rahe hain (folder aur file ka naam)
    filedir, filename = os.path.split(filepath)

    # agar directory ka naam khali nahi hai to directory create karo (agar pehle se hai to error mat do)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    
    # agar file exist nahi karti ya file size 0 hai to empty file create karo
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    # agar file pehle se exist karti hai to message print karo
    else:
        logging.info(f"{filename} is already exists")
