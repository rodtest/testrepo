#!/usr/bin/env python
from git import Repo

repo_dir = ''
repo = Repo(repo_dir)
file_list = [
    'app.py',
    'app2.py'
]
commit_message = 'Add simple ----test'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()

