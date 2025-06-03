# school:JXNU
# author:zouzhou
# createTime: 2025/5/11 23:07

import json
import pandas as pd

with open('data/restbench/tmdb.json') as file:
    re_tmdb = json.load(file)

with open('data/restbench/spotify.json') as file:
    re_spotify = json.load(file)

# 新建一个dataframe，其中有两列，列名分别为requirement和solution
df = pd.DataFrame(re_tmdb, columns=['query', 'solution'])
df_spotify = pd.DataFrame(re_spotify, columns=['query', 'solution'])


df.to_csv('data/restbench/requirement_tmdb.csv', index=False)
df_spotify.to_csv('data/restbench/requirement_spotify.csv', index=False)

