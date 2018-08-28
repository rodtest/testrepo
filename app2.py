#!/usr/bin/env python3
# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------- BASIC IMPORTS AND VARIABLES ------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #
from time import time
import os
import json
from pprint import pprint
# import base64

from github import Github

from CREDENTIALS import CREDENTIAL

current_unix = time()

# ------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------- REPO AND FILE INFO ------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------- #

user = CREDENTIAL['USERNAME']
password = CREDENTIAL['PASSWORD']
g = Github(user, password)

repository = 'githubflask'
repo = g.get_user().get_repo(repository)

payload = "sample.json"
commit_message = 'Updated {payload} at {time}'.format(payload=payload,time=time())

#
# # get the file's SHA
# SHA_output = "user_json.json"
# os.system('curl https://api.github.com/repos/{user}/{repository}/contents/{file} > {SHA_output}'.format(
#                                                                         user=user,
#                                                                         password=password,
#                                                                         repository=repository,
#                                                                         file=payload,
#                                                                         SHA_output=SHA_output))
# with open(SHA_output) as SHA_file:
#     SHA_data = json.loads(SHA_file.read())['sha']
# os.system('rm {}'.format(SHA_output))
#
# # ------------------------------------------------------------------------------------------------------------------- #
# # ------------------------------------------------------ LOGIC ------------------------------------------------------ #
# # ------------------------------------------------------------------------------------------------------------------- #
#
#
# # get the json in string form
# # file = repo.get_file_contents(payload)
# # print(file)
# with open(payload) as f:
#     data = json.dumps(json.loads(f.read())).encode()
# repo.update_file(payload, commit_message, data, SHA_data)


def list_branches():
    # list branches
    os.system('curl https://api.github.com/repos/{user}/{repository}/branches'.format(
        user=user,
        repository=repository
    ))


def get_tree_sha():
    # list branches
    os.system('curl https://api.github.com/repos/{user}/{repository}/branches/master > tree_sha.json'.format(
        user=user,
        repository=repository
    ))
    with open("tree_sha.json") as SHA_file:
        data = json.loads(SHA_file.read())['commit']['commit']['tree']['sha']
    os.system('rm {}'.format("tree_sha.json"))
    return data


def get_parent_sha():
    # list branches
    os.system('curl https://api.github.com/repos/{user}/{repository}/branches > parent_sha.json'.format(
        user=user,
        repository=repository
    ))
    with open("parent_sha.json") as SHA_file:
        data = json.loads(SHA_file.read())
    os.system('rm {}'.format("parent_sha.json"))
    return data


pprint(get_parent_sha())

