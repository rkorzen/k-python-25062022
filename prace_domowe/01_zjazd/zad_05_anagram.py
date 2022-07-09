def is_anagram(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)
    # return set(a) == set(b)


if __name__ == "__main__":
    assert is_anagram("typhoon", "opython") == True
    assert is_anagram("Alice", "Bob") == False
