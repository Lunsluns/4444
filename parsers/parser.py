
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

#Converts text to the Document Object Model
class DocumentParser(object):

    def __init__(self, tokenizer):
        self._tokenizer = tokenizer

    def tokenize_sentences(self, paragraph):
        return self._tokenizer.to_sentences(paragraph)

    def tokenize_words(self, sentence):
        return self._tokenizer.to_words(sentence)