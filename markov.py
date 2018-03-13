"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    f = open(file_path)
    string_file = f.read()

    return string_file


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']   
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    words = text_string.split()
    words.append(None)
    for i in range(len(words) - n):
        #value_list = chains[(words[i], words[i + 1])]
        key = (words[i], words[i + (n - 1)])
        if key in chains:
            chains[key].append(words[i + n])
        else:
            chains[key] = [words[i + n]]

    return chains


def make_text(chains, n):
    """Return text from chains."""
    words = []
    key = choice(chains.keys())
    word = choice(chains[key])
    for i in range(n):
        words.append(key[i - 1])
    while word is not None:
        for i in range(n):
            words.append(word)
            key = (key[i], word)
            word = choice(chains[key])
    return " ".join(words)

# Open the file and turn it into one long string
input_text = open_and_read_file(argv[1])
n = int(argv[2])
# Get a Markov chain
chains = make_chains(input_text, n)

# # Produce random text
random_text = make_text(chains, n)

print random_text