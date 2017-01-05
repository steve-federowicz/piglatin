""" Module to translate english into pig latin """
import re

def move_consonants(word):
    """
    This function moves one or more consonants to the end of a word.  It carries
    out the logic of rule #6
        - A word beginning with multiple consonants should move all of them together to
          the end: "drunk strangers" becomes "unkdray angersstray")

    It also carries out the first half of the logic of rule #1 (e.g. moving the first letter)
        - General rule: take the first letter of a word, move it to the end, and add "ay".
        Example: "hello" becomes "ellohay".


    word: A string containing only alphanumeric characters not starting with a vowel or qu.

    """

    consonants = []
    consec_consonant_flag = True

    for let in word:
        if let not in 'aeiou' and consec_consonant_flag:
            consonants.append(let)
        else:
            consec_consonant_flag = False

    return word[len(consonants):] + ''.join(consonants)


def translate_phrase(phrase):
    """
    Translate an entire phrase by splitting into individual words, calling translate_word()
    for each, and then applying rules 4 and 5 for capitalizatin and punctuation.

    phrase: A string possibly containing a mix of alphanumeric characters and punctuation.

    """
    words = re.split(r"\W+", phrase)
    punctuation = re.findall(r"\W+", phrase)

    punctuation.append('')

    transformed_phrase = ''

    for i, word in enumerate(words):

        if word != '':
            uppercase_flag = word[0].isupper()
            word = word.lower()

            word = translate_word(word)

            if uppercase_flag:
                word = word.capitalize()

        transformed_phrase += word + punctuation[i]

    return transformed_phrase


def translate_word(word):
    """
    Translate an individual word into the appropriate pig latin by applying rules
    1, 3, 6 and 7.

    word: A string containing only alphanumeric characters.

    """

    if word[0] in 'aeiou':
        word += 'w'

    elif word[0:2] == 'qu':
        word = word[2:] + 'qu'

    else:
        word = move_consonants(word)

    word = word + 'ay'

    return word


def main():
    """
    Command line entry point for the piglatin translator.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Translate english to piglatin")

    parser.add_argument("english_phrase", type=str,
                        help="One or more words in sentence form. Single quotes required.")

    args = parser.parse_args()

    piglatin_phrase = translate_phrase(args.english_phrase)

    return piglatin_phrase
