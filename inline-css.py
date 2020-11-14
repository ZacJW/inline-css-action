#!/bin/python3

import premailer, json, os, pathlib

REPO_PATH = pathlib.Path(os.environ['GITHUB_WORKSPACE'])
FILES_LIST = json.loads(os.environ['INPUT_FILES'])

pm = premailer.Premailer()

for file_path_str in FILES_LIST:
    file_path_list = REPO_PATH.glob(file_path_str)
    for file_path in file_path_list:
        with open(file_path, 'r') as file:
            html = pm.transform(file.read())
        with open(file_path, 'w') as file:
            file.write(html)
