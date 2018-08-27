#!/usr/bin/env python
from git import Repo  # pip install GitPython
from time import time

repo_dir = ''  # path to files
repo = Repo(repo_dir)
file_list = [  # list of files to updates in repo_dir
    'app.py',
    'app2.py',
    'app3.py'
]
commit_message = 'Updated {}'.format(time())  # commit message logs unix time
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()



