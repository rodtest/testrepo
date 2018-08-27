#!/usr/bin/env python3
# --------------------------------------------------- #
# ----------- BASIC IMPORTS AND VARIABLES ----------- #
# --------------------------------------------------- #

from github import Github, InputGitTreeElement
from time import time
import base64

from CREDENTIALS import CREDENTIAL

current_unix = time()
user = CREDENTIAL['USERNAME']
password = CREDENTIAL['PASSWORD']

g = Github(user, password)


# --------------------------------------------------- #
# --------------- REPO AND FILE INFO ---------------- #
# --------------------------------------------------- #

repo = g.get_user().get_repo('githubflask')
file_list = ["app.py", "app2.py"]

commit_message = 'Add simple regression analysis'


# --------------------------------------------------- #
# ---------------------- LOGIC ---------------------- #
# --------------------------------------------------- #

master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
element_list = list()
for entry in file_list:
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    element = InputGitTreeElement(entry, '100644', 'blob', data)
    element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
