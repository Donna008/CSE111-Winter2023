import string
import collections

def load_file(filename):
    """
    Loads a text file and returns its contents as a string.

    Parameters:
    filename (str): The name of the text file to load.

    Returns:
    A string containing the contents of the text file.
    """

    try:
        # Open the file for reading
        with open(filename, "r") as f:

            # Read the file contents into a string
            text = f.read()

            return text

    except IOError:
        print(f"Error: File '{filename}' not found or could not be read.")
        return None
    except:
        print("Error: An unexpected error occurred.")
        return None


def count_word_frequency(text, stop_words=[]):
    """
    Counts the frequency of each word in a text string.

    Parameters:
    text (str): The text string to analyze.
    stop_words (list): A list of stop words to remove from the text. Default is an empty list.

    Returns:
    A dictionary where keys are words and values are frequency counts.
    """

    # Remove punctuation and split into words
    words = text.translate(str.maketrans("", "", string.punctuation)).split()

    # Remove stop words and count word frequencies
    word_freq = collections.Counter([word for word in words if word not in stop_words])

    return word_freq


def search_word_frequency(filename, word, stop_words=[]):
    """
    Searches a text file for the frequency of a specific word.

    Parameters:
    filename (str): The name of the text file to analyze.
    word (str): The word to search for.
    stop_words (list): A list of stop words to remove from the text. Default is an empty list.

    Returns:
    The frequency of the specified word in the text file, or 0 if the word is not found.
    """

    # Load the file and count word frequencies
    text = load_file(filename)
    word_freq = count_word_frequency(text, stop_words)

    # Return the frequency of the specified word, or 0 if the word is not found
    return word_freq.get(word.lower(), 0)


def list_word_frequency(filename, stop_words=[]):
    """
    Lists all words in a text file along with their frequencies.

    Parameters:
    filename (str): The name of the text file to analyze.
    stop_words (list): A list of stop words to remove from the text. Default is an empty list.

    Returns:
    A list of tuples where the first element is a word and the second element is its frequency count.
    """

    # Load the file and count word frequencies
    text = load_file(filename)
    word_freq = count_word_frequency(text, stop_words)

    # Convert the word frequencies to a list of tuples and return it
    return list(word_freq.items())


def top_n_word_frequency(filename, n=10, stop_words=[]):
    """
    Lists the top N words by frequency in a text file.

    Parameters:
    filename (str): The name of the text file to analyze.
    n (int): The number of top words to list. Default is 10.
    stop_words (list): A list of stop words to remove from the text. Default is an empty list.

    Returns:
    A list of tuples where the first element is a word and the second element is its frequency count.
    """

    # Load the file and count word frequencies
    text = load_file(filename)
    word_freq = count_word_frequency(text, stop_words)

    # Sort the word frequencies by count and return the top N words
