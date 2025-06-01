import unittest
from src.cinemate.logic import recommend_movies

class TestMovieRecommender(unittest.TestCase):
    def test_exact_match(self):
        result = recommend_movies("drama", "inspiring", "1990s")
        self.assertTrue(any("Shawshank" in m["title"] for m in result))

    def test_fallback_match(self):
        result = recommend_movies("drama", "inspiring", "1980s")
        self.assertTrue(all(m["genre"] == "drama" and m["mood"] == "inspiring" for m in result))

    def test_no_match(self):
        result = recommend_movies("fantasy", "sad", "1960s")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()