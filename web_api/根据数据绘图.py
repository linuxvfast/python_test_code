import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#检查url响应是否正常
repos = requests.get(url)
print('Status_code:',repos.status_code)

#统计总共的仓库数
results = repos.json()
print('Total_repos:',results['total_count'])

#统计仓库的星级
repo_dicts = results['items']
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        if repo_dict['description'] == None:
            plot_dict = {
                'value': repo_dict['stargazers_count'],
                'label': 'none',
                'http': repo_dict['html_url'], #为数据表格添加链接
            }
        else:
            plot_dict = {
               'value':repo_dict['stargazers_count'],
               'label':repo_dict['description'],
                'xlink': repo_dict['html_url'],
           }

        plot_dicts.append(plot_dict)
#
# print(names)
# print(plot_dicts)

#图形显示
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45  #表示x轴旋转45度
my_config.show_legend = False  #表示隐藏图例
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15  #缩短项目名到15个字符
my_config.show_y_guides = False #隐藏水平线
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos3.svg')
