# this file analyzes term frequency
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import math
from pprint import pformat
from collections import Sequence
from _compat import to_unicode, unicode, string_types, Counter


class TfDocumentModel(object):
    """initializes the Term-Frequency document model ( the term = word)."""
    def __init__(self, words, tokenizer=None):
        if isinstance(words, string_types) and tokenizer is None:
            raise ValueError(
                "the tokenizer must be called if 'words' is not a sequence.")
        elif isinstance(words, string_types):
            words = tokenizer.to_words(to_unicode(words))
        elif not isinstance(words, Sequence):
            #error handling
            raise ValueError(
                "Parameter 'words' has to be sequence or string with tokenizer given.")
        self._terms = Counter(map(unicode.lower, words))
        self._max_frequency = max(self._terms.values()) if self._terms else 1

    @property
    def magnitude(self):

        #returns the Length/magnitude of the vector representation of document.
        return math.sqrt(sum(t**2 for t in self._terms.values()))
    #returns the terms
    @property
    def terms(self):
        return self._terms.keys()

    #returns the count (max number of returned terms) of the terms, sorted by frequency in descending order
    def most_frequent_terms(self, count=0):
        # sorts terms by number of occurrences in descending order
        terms = sorted(self._terms.items(), key=lambda i: -i[1])
        #returns a value and returns an error if the count is invalid
        terms = tuple(i[0] for i in terms)
        if count == 0:
            return terms
        elif count > 0:
            return terms[:count]
        else:
            raise ValueError(
                "count must not be negative")
    #returns an int representing the frequency of a specific term
    def term_frequency(self, term):
        return self._terms.get(term, 0)

    #returns the normalized frequency of a term.
    #the smooth is a float whose role is to damp the contribution of the second term, Essentially it scales down the TF by the largest TF in the document.
    def normalized_term_frequency(self, term, smooth=0.0):
        frequency = self.term_frequency(term) / self._max_frequency
        return smooth + (1.0 - smooth)*frequency

    def __repr__(self):
        return "<TfDocumentModel %s>" % pformat(self._terms)