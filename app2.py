#!/usr/bin/env python3
# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------- BASIC IMPORTS AND VARIABLES ------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #
import datetime

import os
import json
from pprint import pprint
# import base64

from github import Github

from CREDENTIALS import CREDENTIAL

current_time = datetime.datetime.now().isoformat()

# ------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------- REPO AND FILE INFO ------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------- #

user = CREDENTIAL['USERNAME']
password = CREDENTIAL['PASSWORD']
g = Github(user, password)

repository = 'githubflask'
repo = g.get_user().get_repo(repository)

payload = "sample.json"
commit_message = '{user} - Updated "{payload}" at {time}'.format(user=user, payload=payload, time=current_time)

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


def get_parent_sha(branch):
    # list branches
    os.system('curl https://api.github.com/repos/{user}/{repository}/branches > parent_sha.json'.format(
        user=user,
        repository=repository
    ))
    with open("parent_sha.json") as SHA_file:
        data = json.loads(SHA_file.read())
    os.system('rm {}'.format("parent_sha.json"))
    data = [x for x in data if x['name'] == branch]
    return data[0]['commit']['sha']


def commit_to_branch(branch):
    json_payload = {
                          "message": commit_message,
                          "author": {
                            "name": user,
                            "date": current_time
                          },
                          "parents": [
                            get_parent_sha(branch)
                          ],
                          "tree": get_tree_sha()
                    }
    url = "https://api.github.com/repos/{user}/{repository}/git/commits".format(user=user, repository=repository)

    curl_string = """curl -d '{json_payload}' -H "Content-Type: application/json" -X POST {url}""".format(
                                                                        json_payload=json.dumps(json_payload),
                                                                        url=url)

    os.system(curl_string)


commit_to_branch("new_branch_test")
