from .logic import recommend_movies

def ask_questions():
    print("Welcome to Cinemate! Let's find a movie for you.\n")
    genre = input("What genre do you prefer? (e.g., drama, sci-fi, crime, romance): ").strip().lower()
    mood = input("What mood are you in? (e.g., inspiring, intense, heartwarming, emotional): ").strip().lower()
    decade = input("Preferred decade? (e.g., 1990s, 2000s, 2010s): ").strip().lower()
    return genre, mood, decade

def main():
    genre, mood, decade = ask_questions()
    movies = recommend_movies(genre, mood, decade)
    if movies:
        print("\nRecommended movies:")
        for movie in movies:
            print(f"- {movie['title']} ({movie['decade']})")
    else:
        print("\nSorry, no exact matches found. Try again with different preferences!")

if __name__ == "__main__":
    main()