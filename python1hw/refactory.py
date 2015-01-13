#!/usr/local/bin/python3
"""here we refactor"""

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    
    >>> book_title('')
    ''
    """
    
    if not title:
        return ''
    
    # 1. create a list of words
    words = title.lower().split()
    new_words = []
    
    # 2. The first word is always capitalized
    new_words.append(words.pop(0).capitalize())
    
    # 3. go through list...
    for w in words:
        # check if prep
        if w in small_words:
            new_words.append(w)
        else:
            new_words.append(w.capitalize())
     
    return(" ".join(new_words))

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()
