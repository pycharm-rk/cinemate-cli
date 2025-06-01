movies = [
    {"title": "The Shawshank Redemption", "genre": "drama", "mood": "inspiring", "decade": "1990s"},
    {"title": "The Godfather", "genre": "crime", "mood": "intense", "decade": "1970s"},
    {"title": "Inception", "genre": "sci-fi", "mood": "mind-bending", "decade": "2010s"},
    {"title": "Forrest Gump", "genre": "drama", "mood": "heartwarming", "decade": "1990s"},
    {"title": "The Matrix", "genre": "sci-fi", "mood": "exciting", "decade": "1990s"},
    {"title": "The Dark Knight", "genre": "action", "mood": "intense", "decade": "2000s"},
    {"title": "Parasite", "genre": "thriller", "mood": "dark", "decade": "2010s"},
    {"title": "Spirited Away", "genre": "animation", "mood": "whimsical", "decade": "2000s"},
    {"title": "Titanic", "genre": "romance", "mood": "emotional", "decade": "1990s"},
    {"title": "Pulp Fiction", "genre": "crime", "mood": "quirky", "decade": "1990s"},
    {"title": "Gladiator", "genre": "action", "mood": "epic", "decade": "2000s"},
    {"title": "The Social Network", "genre": "drama", "mood": "thought-provoking", "decade": "2010s"},
    {"title": "Her", "genre": "sci-fi", "mood": "emotional", "decade": "2010s"},
    {"title": "Amélie", "genre": "romance", "mood": "whimsical", "decade": "2000s"},
    {"title": "Good Will Hunting", "genre": "drama", "mood": "inspiring", "decade": "1990s"},
    {"title": "Whiplash", "genre": "drama", "mood": "intense", "decade": "2010s"},
    {"title": "The Grand Budapest Hotel", "genre": "comedy", "mood": "quirky", "decade": "2010s"},
    {"title": "The Silence of the Lambs", "genre": "thriller", "mood": "intense", "decade": "1990s"},
    {"title": "Requiem for a Dream", "genre": "drama", "mood": "dark", "decade": "2000s"},
    {"title": "Eternal Sunshine of the Spotless Mind", "genre": "romance", "mood": "emotional", "decade": "2000s"},
]

def recommend_movies(genre, mood, decade):
    recommendations = [
        movie for movie in movies
        if movie["genre"] == genre and movie["mood"] == mood and movie["decade"] == decade
    ]
    if not recommendations:
        recommendations = [
            movie for movie in movies
            if movie["genre"] == genre and movie["mood"] == mood
        ]
    return recommendations[:3]