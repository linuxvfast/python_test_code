import requests
#https://api.github.com/将请求发送给github
#search/repositories搜索api上所有的仓库
#？指出传递实参
#language:python为查询主要语言为python的仓库信息
#sort=stars将项目按获得的星级进行排序
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

#检查状态是否正常
result = requests.get(url)
print('Status code:',result.status_code)

#查看总共的仓库数
response_dict = result.json()
print('Total_repos:',response_dict['total_count'])

#统计显示的仓库数
repos_dicts = response_dict['items']
print('Repos_result:',len(repos_dicts))

#获取第一个仓库的信息
# repos_dict = repos_dicts[0]
# print('\nKeys:',len(repos_dict))
# for key in sorted(repos_dict.keys()):
#     print(key)

print('\nSelected information about each repository:')
for repos_dict in repos_dicts:
    print('\nName:',repos_dict['name'])
    print('\nOwner:',repos_dict['owner'])
    print('\nStars:',repos_dict['stargazers_count'])
    print('\nRepository:',repos_dict['html_url'])
    print('\nDescription:',repos_dict['description'])

#查看api限制速率
#https://api.github.com/rate_limit
