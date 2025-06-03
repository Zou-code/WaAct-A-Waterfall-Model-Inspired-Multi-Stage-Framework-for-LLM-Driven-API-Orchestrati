import requests

API_KEY = "538b8673c45719b772aec4f3179e8546"
BASE_URL = "https://api.themoviedb.org/3"

def search_person_by_name(name):
    params = {
        'query': name,
        'api_key': API_KEY
    }
    response = requests.get(f"{BASE_URL}/search/person", params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Error searching person: {response.status_code}")
        return []

def get_person_movie_credits(person_id):
    response = requests.get(f"{BASE_URL}/person/{person_id}/movie_credits", params={'api_key': API_KEY})
    if response.status_code == 200:
        return response.json().get('crew', [])
    else:
        print(f"Error getting person movie credits: {response.status_code}")
        return []

def get_movie_credits(movie_id):
    response = requests.get(f"{BASE_URL}/movie/{movie_id}/credits", params={'api_key': API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting movie credits: {response.status_code}")
        return {'crew': []}

def filter_sole_director_movies(movie_credits_list):
    filtered_movies = []
    for movie in movie_credits_list:
        if movie.get('job') == 'Director':
            movie_id = movie.get('id')
            credits = get_movie_credits(movie_id)
            directors = [crew for crew in credits.get('crew', []) if crew.get('job') == 'Director']
            if len(directors) == 1 and directors[0].get('name') == 'Sofia Coppola':
                filtered_movies.append(movie)
    return filtered_movies

def main():
    person_results = search_person_by_name("Sofia Coppola")
    if not person_results:
        return 0
    sofia_id = person_results[0].get('id')
    movie_credits = get_person_movie_credits(sofia_id)
    sole_directed_movies = filter_sole_director_movies(movie_credits)
    return len(sole_directed_movies)

if __name__ == "__main__":
    print(main())