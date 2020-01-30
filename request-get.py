import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Success!')
    print('Yaaaaayy!')
elif response.status_code == 404:
    print('Not Found.')