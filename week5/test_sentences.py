from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective, get_adverb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_noun = ["bird","boy","car","cat","child","dog","girl","man","rabbit","woman"]
    for _ in range(10):
        word = get_noun(1)
        assert word in single_noun


    plural_noun = ["birds","boys","cars","cats","children","dogs","girls","men","rabbits","women"]
    for _ in range(10):
        word = get_noun(2)
        assert word in plural_noun





def test_get_verb():
    tense_past_verb = ["drank","ate","grew","laughed","thought","ran","slept","talked","walked","wrote"]
    for _ in range(10):
        word = get_verb(1,"past")
        assert word in tense_past_verb

    tense_present_verb1 = ["drinks","eats","grows","laughs","thinks","runs","sleeps","talks","walks","writes"]
    for _ in range(10):
        word = get_verb(1, "present")
        assert word in tense_present_verb1

    tense_presentt_verb = ["drink","eat","grow","laugh","think","run","sleep","talk","walk","write"]
    for _ in range(10):
         word = get_verb(5,"present")
         assert word in tense_presentt_verb

    tense_future_verb = ["will drink","will eat","will grow","will laugh","will think","will run","will sleep","will talk","will walk","will write"]
    for _ in range(10):
        word = get_verb(1,"future")
        assert word in tense_future_verb

def test_get_preposition():
    words = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(30):
        word = get_preposition()
        assert word in words

def test_get_prepositional_phrase():
    determiner_words = ["a", "one", "the","some", "many", "the"]
    preposition_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    noun_words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    quantity = [1,2]
    for i in quantity:
        phrase = get_prepositional_phrase(i)
        words = phrase.split(" ")
        assert words[0] in preposition_words
        assert words[1] in determiner_words
        assert words[2] in noun_words

def test_get_abjective():
    words = ["eager","easy","fair","funny","beautiful","happy","good","frantic","fine","helpful"]
    for _ in range(10):
        word = get_adjective()
        assert word in words

def test_get_adverb():
    words = ["badly","busily","clearly","frankly","hard","really"]
    for _ in range(6):
        word = get_adverb()
        assert word in words




        





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
