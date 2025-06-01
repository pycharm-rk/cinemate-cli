# Cinemate

A simple Python CLI movie recommender that asks a few questions and suggests movies based on your preferences.

## Setup Instructions

1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from https://www.python.org/downloads/

2. **Clone or Download this Project**
   ```bash
   git clone <your-github-repo-url>
   cd cinemate
   ```

   Or, if you downloaded a zip file, unzip it and navigate into the directory.

3. **(Optional) Create Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. **Run the Application**
   ```bash
   python src/cinemate/main.py
   ```

5. **Run Tests**
   ```bash
   python -m unittest discover tests
   ```

## How It Works

- Asks the user 3 questions (genre, mood, and decade).
- Filters a hardcoded movie list based on user preferences.
- Prints up to 3 recommendations or fallback results.

Enjoy your movie night! 🍿
