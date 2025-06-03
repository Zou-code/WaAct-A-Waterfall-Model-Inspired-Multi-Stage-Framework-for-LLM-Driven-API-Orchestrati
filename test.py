# # school:JXNU
# # author:zouzhou
# # createTime: 2025/5/12 14:59
#
import requests

# url = "https://api.themoviedb.org/3/movie/11"
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzhiODY3M2M0NTcxOWI3NzJhZWM0ZjMxNzllODU0NiIsIm5iZiI6MTcxNjAxOTUxMy44ODksInN1YiI6IjY2NDg2MTM5NjU2ZjRjYjhmYWYyM2Y1YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MeP-SVLkuH4a40o4k3EIshuUs0e74OlAE1RVKaPyFNU"
# }
#
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     print(response.json())  # 解析为Python字典
# else:
#     print("Error:", response.status_code)

# API_KEY = "538b8673c45719b772aec4f3179e8546"
# SERVER_URL = "https://api.themoviedb.org/3"
# url = f"{SERVER_URL}/search/person"
# params = {
#     'query': "Sofia Coppola",
#     'api_key': API_KEY
# }
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     data = response.json()
#     if data['results']:
#         print(data)
#         # print(data['results'][0]['id'])
# else:
#     print(f"Error searching person: {response.status_code}")

# import re
#
# requirement = '''\
# ```
# 1. Should the count include only released movies, or also unreleased/in-production movies?
# 2. Should the count be returned as an integer (e.g., 5) or as a string (e.g., "5")?
# 3. Is there a specific time range for the movies to be considered (e.g., only movies directed after a certain year)?
# 4. Should the count include movies where Sofia Coppola was a co-director, or only sole-director credits?
# ```'''
#
# requirement = re.sub(r'^```json\s*|\s*```$', '', requirement, flags=re.MULTILINE)
# print(requirement.strip())



# import requests
#
# url = "https://api.apilayer.com/exchangerates_data/latest?symbols=symbols&base=base"
#
# payload = {}
# headers= {
#   "apikey": "chdAKreKlKD1CJSGYimh17ecMHCs73EU"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
# print(result)


import pandas as pd
#
# df = pd.read_csv('./data/restbench/requirement_tmdb.csv')
#
# # re = '''\ '''
# for _, row in df.iterrows():
#   print(row['query'])
#   print(row['solution'])
#   print()

df = pd.read_csv('./data/restbench/apis/tmdb.csv')

for _, row in df.iterrows():
  print(row['endpoint_name'])
  print(row['endpoint_description'])
  print()

def get_person_birthday(person_id):

  res = requests.get(f'{BASE_URL}/person/{person_id}',
                     params={'api_key': API_KEY})
  return res.json().get('birthday', None)  # birthday 可能为 None














