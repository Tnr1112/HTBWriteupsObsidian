import os
import argparse
import Constants
import re

from hackthebox import HTBClient

def glob_re(pattern, strings):
    return filter(re.compile(pattern).match, strings)

# Params
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-m", "--machine_name", help="Input of the machine", default="",required=True)
parser.add_argument("-v", "--vault_path", help="Path of obsidian vault", default="",required=True)
args = parser.parse_args()

machine_name = args.machine_name 
VAULT_PATH = args.vault_path
MACHINE_FOLDER_PATH = VAULT_PATH + "Machines/" + machine_name

if os.path.exists(MACHINE_FOLDER_PATH):
    mdFileNames = list(glob_re(r'^\d{2}.*[.md]$', os.listdir(MACHINE_FOLDER_PATH)))
    if len(mdFileNames) > 0:
        with open(os.path.join(MACHINE_FOLDER_PATH, f"Writeup{machine_name}.md"), 'w', encoding="utf-8") as writeupFile:
            for mdFilename in mdFileNames:
                with open(os.path.join(MACHINE_FOLDER_PATH , mdFilename), 'r', encoding="utf-8") as temp_file:
                    writeupFile.write(temp_file.read())
                print(f"Writing {mdFilename}")
    else:
        print(f"No .md files in {MACHINE_FOLDER_PATH}.")
else:
    print(f"Error {MACHINE_FOLDER_PATH} doesn't exists.")

print("Exiting...")