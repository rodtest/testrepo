from flask import Flask, request, url_for, redirect, flash
from flask_github import GitHub

from CREDENTIALS import CREDENTIAL

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = CREDENTIAL['GITHUB_CLIENT_ID']
app.config['GITHUB_CLIENT_SECRET'] = CREDENTIAL['GITHUB_CLIENT_SECRET']

# For GitHub Enterprise
app.config['GITHUB_BASE_URL'] = 'https://api.github.com/'               # different for GitHub Enterprise
app.config['GITHUB_AUTH_URL'] = 'https://github.com/login/oauth/'       # different for GitHub Enterprise

github = GitHub(app)


@app.route('/login')
def login():
    return github.authorize()


@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.github_access_token


@app.route('/repo')
def repo():
    repo_dict = github.get('repos/{user}/{repo}'.format(user=CREDENTIAL['USERNAME'], repo="dotfiles"))
    return str(repo_dict)


if __name__ == "__main__":
    app.run(debug=True)