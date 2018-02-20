GithubCountPy
=====
GithubCountPy is a very simple module to count watch, fork, star, commit and etc. for specific repositories.

No user, password and access token needed.


### Sample code
```python
from GithubCountPy import repos_count

count_repos = repos_count('django/django', 'pallets/flask')
print(count_repos)

# output below
#[{'name': 'django/django', 'watch': 1918,
#'star': 31868...}, {'name': 'pallets/flask',
#'watch': 1944, 'star': 33284...}]
```

### API
Github's API V3 is used for counts including watch, star, fork, open_issues, lang and created_time.

### Scraper
Though you could use Github API to retrieve the data from repositories, there are many limitations. First, there is no access to count commits. Second, you need to deal with multiple pages to sum the number of contributors. Third, there is rate limit to call the API. Scraper is used to retrieve the count of commits, branches, releases and contributors. 

### Links
Github API V3: https://developer.github.com/v3/
