import requests

# scope=talk_message, 이거 안넣어주면 403 에러 발생
get_token_url = 'https://kauth.kakao.com/oauth/authorize?client_id={api_key}&redirect_uri={redirect_uri}&response_type=code&scope=talk_message'

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = ''
redirect_uri = ''
authorize_code = '' # access token

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)