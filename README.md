GithubCountPy is a very simple module to count watch, fork, star, commit and etc. for specific repositories.

No user, password and access token needed.


### Sample code
```
from GithubCountPy import repos_count

count_repos = repos_count('django/django', 'pallets/flask')
print(count_repos)

# output below
#[{'name': 'django/django', 'watch': 1918,
#'star': 31868...}, {'name': 'pallets/flask',
#'watch': 1944, 'star': 33284...}]
```

### API
Github's API V3 is used to count follower's data including watch, star, fork, open_issues, lang and created_time.

### Scraper
Even though you could use Github API to get the repositories' data, there are many limitations. First, there is no access to count commits. Second, you need to deal with multiple pages to sum the number of contributors. Third, there is rate limit to call the API.

### Links
Github API V3: https://developer.github.com/v3/
