import requests
from operator import itemgetter

url = 'https://news.ycombinator.com//v0/topstories.json'
result = requests.get(url)
print('status_code:',result.status_code)

result_dicts = result.json()
count_dicts = []
for id in result_dicts[:30]:
    url = ('https://news.ycombinator.com//v0/item/' + str(id) + '.json')
    count_repos = requests.get(url)
    print(count_repos.status_code)
    response_dict = count_repos.json()
    count_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id=' + str(id),
        'comments':response_dict.get('descendants',0)
    }
    count_dicts.append(count_dict)

count_dicts = sorted(count_dicts,key=itemgetter('comments'),reverse=True)

for dict in count_dicts:
    print("\nTitle:",dict['title'])
    print('Discussion link:',dict['link'])
    print('Comments:',dict['comments'])

