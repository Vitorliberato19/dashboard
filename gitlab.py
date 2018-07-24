import requests

TOKEN = 'Y3jgjt-mdLKszrnQsSic'
# GITLAB = 'http://192.168.0.100/api/v4/projects?private_token={tk}'
GITLAB = 'http://192.168.0.100/api/v4/{route}?private_token={tk}'

# response = requests.get(GITLAB.format(tk=TOKEN, route='projects'))
# for x in response.json():
#     print('{} -{}'.format(x['id'], x['path']))
# exit()
# repository = {'name' : 'flask-app'}
# response = requests.post(GITLAB.format(tk=TOKEN), repository)
# print(response.json())


response = requests.get(GITLAB.format(tk=TOKEN,route='users'))
# print(response.json())

# for x in response.json():
#     print(x['id'], x['name'])
# exit()
# user = {'email':'vitor@vitor.com.br',
#         'username': 'vitor',
#         'name':'vitor',
#         'password':'vitor123' }

# response = requests.post(GITLAB.format(tk=TOKEN, route='users'), user)
# print(response.json())

pit = 4
member = {'user_id':3,'access_level':40}
response = requests.post('http://192.168.0.100/api/v4/projects/{pid}/members?private_token={tk}'.format(pid=4, tk=TOKEN),member)


