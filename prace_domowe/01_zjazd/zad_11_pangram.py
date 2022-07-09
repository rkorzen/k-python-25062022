import string, sys


def ispangram(str1, alphabet=string.ascii_lowercase):
    # print(alphabet)
    alphaset = set(alphabet)

    return alphaset <= set(str1.lower())


def test_ispangram():
    assert ispangram("The quick brown fox jumps over the lazy dog") == True
    assert ispangram("Ala ma kota") == False

    alphabet = string.ascii_lowercase + "ąćęłńóśźż"
    alphabet = list(alphabet)
    alphabet.remove("q")
    alphabet.remove("x")
    alphabet.remove("v")

    assert (
        ispangram("Pchnąć w tę łódź jeża lub ośm skrzyń fig", alphabet=alphabet) == True
    )
