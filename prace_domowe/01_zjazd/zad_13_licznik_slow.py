from collections import Counter
import re

word_pattern = re.compile(r"\b[\w'-]+\b")


def count_words(words):
    words = word_pattern.findall(words.lower())
    return Counter(words)


class TestCountWords:
    def test_simple_sentence(self):
        actual = count_words("kobyła ma mały bok bok")
        expected = {"kobyła": 1, "ma": 1, "mały": 1, "bok": 2}
        assert actual == expected

    def test_ignore_capitalization(self):
        actual = count_words("kobyła ma mały bok Bok")
        expected = {"kobyła": 1, "ma": 1, "mały": 1, "bok": 2}
        assert actual == expected

    def test_ignore_punctations(self):
        actual = count_words("kobyła, ma mały bok! Bok!")
        expected = {"kobyła": 1, "ma": 1, "mały": 1, "bok": 2}
        assert actual == expected
        actual = count_words("¿Te gusta Python?")
        expected = {"te": 1, "gusta": 1, "python": 1}
        assert actual == expected

    def test_apostrophe_and_dash(self):
        actual = count_words("C'est la vie, c'est la vie! ")
        expected = {"c'est": 2, "la": 2, "vie": 2}
        assert actual == expected

        actual = count_words("C'est la vie, -- c'est la vie! closed-door")
        expected = {"c'est": 2, "la": 2, "vie": 2, "closed-door": 1}
        assert actual == expected

        actual = count_words("Co-")
        expected = {"co": 1}
        assert actual == expected

        actual = count_words("cos'")
        expected = {"cos": 1}
        assert actual == expected

        actual = count_words("co-to")
        expected = {"co-to": 1}
        assert actual == expected

        actual = count_words("co!to")
        expected = {"co": 1, "to": 1}
        assert actual == expected
