""" Unit test for piglatin translation """

from piglatin import translator

def test_move_consonants():
    """
    Individually test the function which moves one or consonants to the end.
    """
    word_pairs = [('hello', 'elloh'), ('world', 'orldw'),
                  ('drunk', 'unkdr'), ('strangers', 'angersstr')]


    for english, piglatin in word_pairs:
        assert piglatin == translator.move_consonants(english)


def test_translate_word():
    """
    Check that all of the word translation rules are working in concert.
    """
    word_pairs = [('hello', 'ellohay'), ('world', 'orldway'),
                  ('drunk', 'unkdray'), ('strangers', 'angersstray'),
                  ('eat', 'eatway'), ('apples', 'applesway')]

    for english, piglatin in word_pairs:
        assert piglatin == translator.translate_word(english)


def test_translate_phrase():
    """
    Check that full phrase translation is working correctly.
    """
    phrase_pairs = [('hello world', 'ellohay orldway'),
                    ('drunk strangers', 'unkdray angersstray'),
                    ('quickly and quietly', 'icklyquay andway ietlyquay'),
                    ('eat apples', 'eatway applesway'),
                    ('Hello world', 'Ellohay orldway'),
                    ('Hello, world!', 'Ellohay, orldway!'),
                    ('Hello, world!!', 'Ellohay, orldway!!'),
                    ('Hello , world!', 'Ellohay , orldway!'),
                    ('#Hello , #world!', '#Ellohay , #orldway!'),
                    ('Hello, world !', 'Ellohay, orldway !')]

    for english, piglatin in phrase_pairs:
        assert piglatin == translator.translate_phrase(english)


def test_edge_cases():
    """
    Check a few UI edge cases
    """

    edge_cases = [(',', ','),
                  (', ,', ', ,')]

    for english, piglatin in edge_cases:
        assert piglatin == translator.translate_phrase(english)
