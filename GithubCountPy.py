from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import json

def count_user(repo):
    r = requests.get('https://api.github.com/repos/{}'.format(repo))
    if r.ok:
        repoItem = json.loads(r.text or r.content)
        return repoItem['subscribers_count'], repoItem['stargazers_count'], \
               repoItem['forks_count'], repoItem['open_issues_count'], repoItem['language'], repoItem['created_at']

def count_master(repo):
    html = urlopen("https://github.com/{}".format(repo))
    soup = BeautifulSoup(html, 'html.parser')

    # commit
    commits_box = soup.find('li', attrs={'class': "commits"}).find('span')
    commits_text = commits_box.contents[0].strip()
    commits_int = int(commits_text.replace(',', ''))

    # branches
    branches_box = soup.find('a', href=re.compile("/{}/branches".format(repo))).find('span')
    branches_text = branches_box.contents[0].strip()
    branches_int = int(branches_text.replace(',', ''))

    # releases
    releases_box = soup.find('a', href=re.compile("/{}/releases".format(repo))).find('span')
    releases_text = releases_box.contents[0].strip()
    releases_int = int(releases_text.replace(',', ''))

    # contributors
    contributors_box = soup.find('a', href=re.compile("/{}/graphs/contributors".format(repo))).find('span')
    contributors_text = contributors_box.contents[0].strip()
    contributors_int = int(contributors_text.replace(',', ''))
    return commits_int, branches_int, releases_int, contributors_int

def repos_count(*repos):
    repos_list = []
    for repo in repos:
        if repo[0] == '/':
            repo = repo[1:]
        repo_dict = {}
        watch, star, fork, open_issues, lang, created_time = count_user(repo)
        commits, branches, releases, contributors = count_master(repo)
        repo_dict['name'] = repo
        repo_dict['watch'] = watch
        repo_dict['star'] = star
        repo_dict['fork'] = fork
        repo_dict['open_issues'] = open_issues
        repo_dict['lang'] = lang
        repo_dict['created_time'] = created_time

        repo_dict['commits'] = commits
        repo_dict['branches'] = branches
        repo_dict['releases'] = releases
        repo_dict['contributors'] = contributors

        repos_list.append(repo_dict)

    return repos_list




