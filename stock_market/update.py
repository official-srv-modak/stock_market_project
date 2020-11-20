""" This is used to update the code

AUTHOR - SOURAV MODAK
DATE - 20 NOV 2020
INDIA

"""

import os, subprocess
from support import give_pop_up_dialog

repository_url = "https://github.com/official-srv-modak/StockAll.git"
update_file_path = "update.bat"

def get_local_revision():
    result = subprocess.run("git parse HEAD", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    local_version = str(result.stdout).split("'")[1].split("\\")[0]
    print(local_version)
    return local_version

def get_remote_repo_version(repository_url):
    result = subprocess.run("git ls-remote "+repository_url+" HEAD", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    remote_version = str(result.stdout).split("'")[1].split("\\")[0]
    print(remote_version)
    return remote_version

def update_file():
    filehandle = open(update_file_path, 'w')
    StartName = "StockAll.exe"
    filehandle.write("timeout 5\ntaskkill /IM \"StockAll.exe\"\nwmic Path win32_process Where \"CommandLine Like '"+StartName+"'\" Call Terminate\n")
    filehandle.write("git stash\ngit pull\n")
    filehandle.write("timeout 5\nAutoTut.exe\nexit\n")
    filehandle.close()
    os.system("start \"\" "+update_file_path)

def check_and_update_package():
    local_version = get_local_revision()
    remote_version = get_remote_repo_version(repository_url)
    if local_version != remote_version:
        give_pop_up_dialog("New update detected, the system will update", 100, 400, True)


def update():
    local_version = get_local_revision()
    remote_version = get_remote_repo_version(repository_url)

update()