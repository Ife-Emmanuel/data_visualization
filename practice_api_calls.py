"""To make an API call"""
import requests
from plotly import offline
from plotly.graph_objs import Bar
url = r'https://api.github.com/search/repositories?q=language:python&sort=Stars'
r = requests.get(url)
print('Status code : ', r.status_code)

# Storing the api response in a variable
reponse_dict = r.json()
repo_dicts = reponse_dict['items']
print('Total repositories : ', reponse_dict['total_count'])
first_repo = repo_dicts[0]
print('Selected information about first repository : ')
print('Name : ', first_repo['name'])
print('Owner : ', first_repo['owner']['login'])
print('Stars : ', first_repo['stargazers_count'])
print('Repository : ', first_repo['html_url'])
print('Created : ', first_repo['created_at'])
print('Updated : ', first_repo['updated_at'])
print('Description : ', first_repo['description'])
# for key in sorted(rep)
print(len(repo_dicts))
print(repo_dicts)

names, stars, repo_links = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    names.append(repo_name)
    star = repo_dict['stargazers_count']
    stars.append(star)
    html_url = repo_dict['html_url']
    repo_link = f"<a href= '{html_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

data = [{'type' : 'bar',
         'x' : repo_links,
         'y' : stars,
         'marker' : {'color' : 'rgb(0, 0, 100)',
                     'line' : {'width' : 1.5, 'color' : 'rgb(25, 25, 25)'},
                     },
         'opacity' : 0.6

         }]

layout = {'title' : 'repositories_stars_rate'.title(),
          'titlefont' : {'size' : 28},

          'xaxis' : {'title' : 'Repository',
                     'titlefont' : {'size' : 24},
                     'tickfont' : {'size' : 14}},
          'yaxis' : {'title' : 'Stars',
                     'titlefont' : {'size' : 24},
                     'tickfont' : {'size' : 14}}}


fig = {'data' : data, 'layout' : layout }
offline.plot(fig, 'repositories_stars_rate.html')

# for i, repo_dict in enumerate(repo_dict):
#     print(i + 1, repo_dict['owner']['login'])
# for subject, value in reponse_dict

# Now I want to create a visualization based on the count of stars for each repositories.


