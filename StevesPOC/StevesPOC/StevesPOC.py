import requests

credentials = '{email}', '{password}'
session = requests.Session()
session.auth = credentials

github = 'https://api.github.com'

response = session.get(github)
if response.status_code != 200:
    print('There be errors here! {}'.format(response.status_code))
    exit()
data = response.text
print(data)