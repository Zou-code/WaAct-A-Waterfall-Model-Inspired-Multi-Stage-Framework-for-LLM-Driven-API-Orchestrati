# school:JXNU
# author:zouzhou
# createTime: 2025/5/12 14:00

"""提取API的json文件中的关键信息，保存到一个csv文件中"""

import json
import pandas

TMDB_FILE = "restbench/apis/reduced_tmdb.json"
SPOTIFY_FILE = "restbench/apis/reduced_spotify.json"

def tmdn_extract():
    with open(TMDB_FILE, "r", encoding="utf-8") as f:
        tqdm_data = json.load(f)

    data = []

    server_url = tqdm_data["servers"][0].get("url")
    endpoints = tqdm_data["endpoints"]
    for endpoint in endpoints:
        endpoint_name = endpoint[0]
        endpoint_description = endpoint[2].get("description")
        parameters = endpoint[2].get("parameters")
        if parameters is None:
            parameters = " "
        response_schema = endpoint[2].get("responses").get("content").get("application/json").get("schema")
        response_example = endpoint[2].get("responses").get("content").get("application/json").get("examples").get("response").get("value")
        response_example = " "
        data.append({"endpoint_name": endpoint_name,
                     "endpoint_description": endpoint_description,
                     "parameters": parameters,
                     "response_schema": response_schema,
                     "response_example": response_example,
                     "server_url": server_url})
    df = pandas.DataFrame(data)
    df.to_csv("restbench/apis/spotify.csv", index=False)


def spotify_extract():
    with open(SPOTIFY_FILE, "r", encoding="utf-8") as f:
        tqdm_data = json.load(f)

    data = []

    server_url = tqdm_data["servers"][0].get("url")
    endpoints = tqdm_data["endpoints"]
    for endpoint in endpoints:
        endpoint_name = endpoint[0]
        endpoint_description = endpoint[2].get("description")
        parameters = endpoint[2].get("parameters")
        if parameters is None:
            parameters = " "
        try:
            response_schema = endpoint[2].get("responses").get("content").get("application/json").get("schema")
        except Exception as e:
            response_schema = ""
            print(e)
        # response_example = endpoint[2].get("responses").get("content").get("application/json").get("examples").get("response").get("value")
        response_example = " "
        data.append({"endpoint_name": endpoint_name,
                     "endpoint_description": endpoint_description,
                     "parameters": parameters,
                     "response_schema": response_schema,
                     "response_example": response_example,
                     "server_url": server_url})
    df = pandas.DataFrame(data)
    df.to_csv("restbench/apis/spotify.csv", index=False)

if __name__ == '__main__':
    spotify_extract()



