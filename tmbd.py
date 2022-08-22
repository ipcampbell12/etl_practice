import pandas as pd
import requests
import config

response_list = []

API_KEY = config.api_key

for movie_id in range(550, 556):
    url = url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(
        movie_id, API_KEY)
    r = requests.get(url)
    response_list.append(r.json())


df = pd.DataFrame.from_dict(response_list)
print(df)
